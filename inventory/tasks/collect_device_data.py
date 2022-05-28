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

@shared_task(bind=True, track_started=True, name='Collect data from single device')
def collect_device_data(self, device_id: int = False) -> bool:
    """ Collect data from single device, using SSH protocol. """

    def check_output_status(output):
        if output == {} or output == [] or output is None or output is False:
            return False
        else:
            return True

    # Count successful outputs:
    successful = 0
    # Declare collected data:
    collected_data = None
    # Collect all data from device:
    device = Device.objects.get(pk=device_id)
    connection = NetCon(device).open_connection()
    if connection:
        collected_data = connection.execute_device_type_templates()
        connection.close_connection()
    # Create new update object:
    new_device_update_object = DeviceUpdate.objects.create(
        device=device, status=0)
    # Iterate thru all collected data:
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
        # Create single device collected data object:
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
    # Create message:
    commands_count = len(collected_data)
    if commands_count > 1:
        message = f'Successfully collected {successful} commands outputs from {commands_count} commands.'
    else:
        message = f'Successfully collected {successful} command outputs from {commands_count} command.'
    async_to_sync(channel_layer.group_send)('collect', {'type': 'device_update', 'text': message})
    return message

