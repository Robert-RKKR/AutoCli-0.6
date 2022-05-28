# Models Import:
from this import d
from inventory.models.device_collected_data_model import DeviceCollectedData
from inventory.models.device_update_model import DeviceUpdate
from inventory.models.device_model import Device

# File reader Import:
from inventory.yaml_reader import yaml_read

# Constance Import:
from inventory.constants import DEVICE_TYPES

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
logger = Logger('SSH Netconf connection')

# Channels variable:
channel_layer = get_channel_layer()

def single_device_update(device_pk: int, request_id: int) -> bool:
    """ Collect data from device, using SSH protocol. """

    def check_output_status(output):

        if output == {} or output == [] or output is None or output is False:
            return False
        else:
            return True

    # Check if device_pk variable is integer:
    if isinstance(device_pk, int):

        try: # Find Device object by ID:
            device = Device.objects.get(pk=device_pk)

        except:
            # Log 404 device error:
            logger.error(f'Device with ID {device_pk}, is not available.', request_id)
            return False

        else:
            # Log starting of device data collection:
            logger.info(f'Starting of device {device.name} ({device.hostname}), data collection', request_id, device)

            # Start device SSH connection:
            connection = NetCon(device, request_id)
            connection.open_connection()

            # Collect device types template:
            device_types_template = yaml_read(DEVICE_TYPES)['output']
            # Collect device types commands:
            device_types_commands = device_types_template.get(device.device_type, {}).get('commands', False)
            # Collect command outputs from device:
            if device_types_commands and connection:
                device_output = connection.enabled_commands(device_types_commands)
                connection.close_connection()
            else:
                return connection

            # End data rapport:
            end_data_rapport = {
                'count': 0
            }

            # Save collected data to database:
            try:
                device_update_object = DeviceUpdate.objects.create(
                    device=device,
                    result_status=True
                )
                # Loop thru all commands:
                for command in device_output:
                    # Collect basic data:
                    raw_data = device_output[command].get('command_output', False),
                    processed_data = device_output[command].get('processed_output', False)
                    # Collect data to end data rapport:
                    raw_data_status = check_output_status(raw_data)
                    processed_data_status = check_output_status(processed_data)
                    if raw_data_status and processed_data_status:
                        result_status = True
                        # Increase counter:
                        end_data_rapport['count'] += 1
                    else:
                        result_status = False
                    # Save collected command output to database:
                    DeviceCollectedData.objects.create(
                        update=device_update_object,
                        command_name=command,
                        command_raw_data=raw_data,
                        command_processed_data=processed_data,
                        raw_data_status=raw_data_status,
                        processed_data_status=processed_data_status,
                        result_status=result_status
                    )
                    # Create end data rapport:
                    end_data_rapport[command] = result_status
            except:
                return False
            else:
                return end_data_rapport

    else: # If device variable is not a integer, raise type error:
        raise TypeError('Device PK variable can only be a integer.')

@shared_task(bind=True, track_started=True, name='Collect data from device')
def collect_device_data(self, devices: int or str = False) -> bool:
    """ Collect data from device, using SSH protocol. """

    success_count = 0
    devices_count = 0

    # Check if devices value was provided:
    if devices:

        # Collect data from one device:
        if isinstance(devices, int):
            # Collect data from device:
            response = single_device_update(devices, self.request.id)
            if response['count'] > 0:
                success_count = 1
            devices_count = 1
    
        # Collect data from multiple devices:
        elif isinstance(devices, list):
            for device in devices:
                # Collect data from device:
                response = single_device_update(device, self.request.id)
                # Collect data to rapport:
                devices_count += 1
                if response['count'] > 0:
                    success_count += 1

        # Return False:
        else:
            return False

    else:

        # Update all devices from database:
        pass

    # Send async to sync message:
    if devices_count == 1:
        if success_count == 1:
            message = f'Successfully updated one device.'
        else:
            message = f'Unfortunately device was not updated.'
    else:
        message = f'Successfully updated {success_count} for {devices_count} device/s.'
    async_to_sync(channel_layer.group_send)('collect', {'type': 'device_update', 'text': message})
    return message
