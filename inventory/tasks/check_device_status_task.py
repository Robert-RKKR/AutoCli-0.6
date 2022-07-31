# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Base task Import:
from email import message
from autocli.basetask.basetask import BaseTask

# NetCon Import:
from inventory.connections.netcon import NetCon

# Celery application Import:
from autocli.celery import app


# Test taks class:
class CheckDeviceStatus(BaseTask):
    """
    Check status of device or devices, using SSH / HTTPS protocol.
    Usage: CheckDeviceStatus.delay(<pk value>)

    Parameters:
    -----------------
    pk: integer, string or list
        int = return one device data collection.
        list = return multiple devices data collection.
        str 'all' = return all active devices data collection.
    
    Steps to follow:
    1. 
    2. 
    3. 
    4. 
    5. 
    6. 
    """

    name = 'Check device status'
    description = 'Check status of device or devices, using SSH / HTTPS protocol.'
    logger_name = 'Check device status'
    # queue = 'status_check'
    queue = 'status_update'

    def _run(self, pk, *args, **kwargs):
        # Collect all device objects based on provided pk value:
        collected_objects = self._collect_device_objects(pk)
        # Verify that the object was collected correctly:
        if collected_objects:

            # Iterate thru all collected device objects:
            for collected_device_object in collected_objects:

                # Update globally accessible variables:
                self.corelate_object = collected_device_object
                self.corelate_object_name = collected_device_object.name

                # Confect to device using NetCon class:
                ssh_connection = NetCon(collected_device_object, self.task_id, 1).test_connection()
                if ssh_connection:
                    collected_device_object.ssh_status = True
                    message = f"Status of device {self.corelate_object_name} was checked, device is active."
                    # Send message to channel:
                    self.send_message(message, self.queue, 2)
                else:
                    collected_device_object.ssh_status = False
                    message = f"Status of device {self.corelate_object_name} was checked, device is not active."
                    # Send message to channel:
                    self.send_message(message, self.queue, 1)
                # Update device object:
                collected_device_object.save(update_fields=['ssh_status'])
                # Log status update:
                self.logger.info(message, self.task_id, self.corelate_object_name)

        else:
            # Log data collection error:
            self.logger.warning('An error occurred during attempt to collect provided device/s, based on PK.',
                self.task_id, self.corelate_object_name)
            # Log data collection user error:
            self.logger.warning('An error occurred during data collection (NR. 374521553764).',
                self.task_id, self.corelate_object_name, True)

# Task registration:
CheckDeviceStatus = app.register_task(CheckDeviceStatus())
