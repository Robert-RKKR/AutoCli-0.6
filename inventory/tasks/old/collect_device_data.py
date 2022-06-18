# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Django Import:
import time

# Models Import:
from inventory.models.device_collected_data_model import DeviceCollectedData
from inventory.models.device_update_model import DeviceUpdate
from inventory.models.device_model import Device

# Django exception Import:
from django.db import IntegrityError

# NetCon Import:
from inventory.connections.netcon import NetCon

# Logger import:
from logger.logger import Logger

# Celery Import:
from celery import shared_task
from autocli.celery import app
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Logger class initiation:
logger = Logger('Collecting data')

# Channels variable:
channel_layer = get_channel_layer()

@shared_task(bind=True, track_started=True, name='Collect data from single device')
def collect_device_data(self, device_id: int, request_id: str = False) -> bool:
    """ Collect data from single device, using SSH protocol. """

    # Check command output:
    def check_output_status(output):
        if output == {} or output == [] or output is None or output is False:
            return False
        else:
            return True

    # Self ID declaration:
    if request_id is False:
        request_id = self.request.id
    # Return data:
    return_data = {
        'message': None,
        'successful': None,
        'commands_count': None,
        'status': None}
    # Count successful outputs:
    successful = 0
    commands_count = 0
    # Start clock count:
    start_time = time.perf_counter()
    # Declare collected data:
    collected_data = None
    try: # Try to collect device from database:
        device = Device.objects.get(pk=device_id)
        logger.info(
            f'Process of collecting information from {device.name} has been started',
            request_id, device.name)
    except:
        pass
    else:
        # Collect all data from device:
        connection = NetCon(device, request_id).open_connection()
        if connection:
            collected_data = connection.execute_device_type_templates()
            connection.close_connection()
        try: # Try to create new update object:
            new_device_update_object = DeviceUpdate.objects.create(
                device=device, status=0)
        except IntegrityError as error:
            logger.debug(
                f'Process of creating device update object fails, on device {device.name}.\n{error}',
                request_id, device.name)
        
        # Finish clock count & method execution time:
        finish_time = time.perf_counter()
        connection_time = round(finish_time - start_time, 5)
        
        # Iterate thru all collected data:
        if collected_data:
            # Defiant command count:
            commands_count = len(collected_data)
            for single_command_output in collected_data:
                # Collect data:
                command_name=single_command_output['command']
                command_raw_data=single_command_output['command_output']
                command_processed_data=single_command_output['processed_output']
                raw_data_status = check_output_status(command_raw_data)
                processed_data_status = check_output_status(command_processed_data)
                if processed_data_status and raw_data_status:
                    result_status = True
                    successful += 1
                else:
                    result_status = False
                try: # Try to create single device collected data object:
                    DeviceCollectedData.objects.create(
                        # Update corelation:
                        device_update=new_device_update_object,
                        # Collected command data:
                        command_name=command_name,
                        command_raw_data=command_raw_data,
                        command_processed_data=command_processed_data,
                        # Collected command data status:
                        result_status=result_status,
                        raw_data_status=raw_data_status,
                        processed_data_status=processed_data_status,
                    )
                except IntegrityError as error:
                    logger.debug(
                        f'Process of creating device collected data object fails, '\
                        'on device {device.name}.\n{error}',
                        request_id, device.name)

            # Log end of process:
            if successful > 0:
                logger.info(
                    f'Process of collecting information from {device.name} '\
                    f'has been accomplish (Collected {successful} outputs from {commands_count} commands). '\
                    f'Execution time {connection_time} seconds.',
                    request_id, device.name)
            else:
                logger.warning(
                    f'Process of collecting information from {device.name} has failed. '\
                    f'Execution time {connection_time} seconds.',
                    request_id, device.name)
            # Create message:
            message = f'Successfully collected {successful} output/s '\
            f'outputs from {commands_count} command/s, on device {device.name}. '\
            f'Execution time {connection_time} seconds.'
            # Upgrade rerun data:
            return_data['status'] = True

        else:
            # Create message:
            message = f'Data could not be collected from device {device.name}'
            # Log end of process:
            logger.warning(message,request_id, device.name)
            # Upgrade rerun data:
            return_data['status'] = False
            
        # Send message to async_to_sync:
        async_to_sync(channel_layer.group_send)('collect', {'type': 'send_collect', 'text': message})
        # Upgrade rerun data:
        return_data['message'] = message
        return_data['successful'] = successful
        return_data['commands_count'] = commands_count
        # Return return data
        return return_data


@shared_task(bind=True, track_started=True, name='Collect data from all devices')
def collect_all_devices_data(self) -> bool:

    # Start clock count:
    start_time = time.perf_counter()
    # Self ID declaration:
    request_id = self.request.id
    # Return data:
    return_data = {
        'message': None,
        'successful': None,
        'devices_counter': None}
    try: # Try to collect all active devices:
        all_active_devices_list = Device.objects.filter(active=True)
    except:
        pass
    else:
        # Counters declaration:
        successful = 0
        devices_counter = len(all_active_devices_list)
        # Iterate thru all collected devices:
        for device in all_active_devices_list:
            output = collect_device_data(device.pk, request_id)
            if output['status'] is True:
                successful += 1

    # Finish clock count & method execution time:
    finish_time = time.perf_counter()
    connection_time = round(finish_time - start_time, 5)
    
    # Create message:
    message = f'Process of collecting information from all devices '\
    f'has been accomplish (Successfully collected data from {successful} '\
    f'device out of {devices_counter} available in {connection_time} seconds).'
    logger.info(message, request_id, device.name)
    # Send message to async_to_sync:
    async_to_sync(channel_layer.group_send)('collect', {'type': 'send_collect', 'text': message})
    # Upgrade rerun data:
    return_data['message'] = message
    return_data['successful'] = successful
    return_data['devices_counter'] = devices_counter
    # Return return data
    return return_data
