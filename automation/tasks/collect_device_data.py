# Models Import:
from inventory.models.device_collected_data_model import DeviceCollectedData
from automation.models.device_update_model import DeviceUpdate
from inventory.models.device_model import Device

# File reader Import:
from automation.connections.yaml_reader import yaml_read

# Constance Import:
from automation.constants import DEVICE_TYPES

# NetCon Import:
from automation.connections.netcon import NetCon

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

    # Check if device_pk variable is intiger:
    if isinstance(device_pk, int):

        try: # Find Device object by ID:
            device = Device.objects.get(pk=device_pk)

        except:
            # Log 404 device error:
            logger.error(f'Device with ID {device_pk}, is not avaliable (Error 404).', request_id)
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
                return False

            # Save collected data to database:
            device_update_object = DeviceUpdate.objects.create(
                device=device,
                result_status=True
            )
            for command in device_output:
                raw_data = device_output[command].get('command_output', False),
                processed_data = device_output[command].get('proccessed_output', False)
                DeviceCollectedData.objects.create(
                    update=device_update_object,
                    command_name=command,
                    command_raw_data=raw_data,
                    command_processed_data=processed_data
                )

            # Return:
            return True

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('Device PK variable can only be a intiger.')

@shared_task(bind=True, track_started=True, name='Collect data from device')
def collect_device_data(self, devices: int or str = False) -> bool:
    """ Collect data from device, using SSH protocol. """

    # Check if devices value was provided:
    if devices:

        # Collect data from one device:
        if isinstance(devices, int):
            return single_device_update(devices, self.request.id)
    
        # Collect data from multiple devices:
        elif isinstance(devices, list):
            pass

        # Return False:
        else:
            return False

    else:

        # Update all devices from database:
        pass
