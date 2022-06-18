# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Base task Import:
from autocli.basetask.basetask import BaseTask

# Models Import:
from inventory.models.device_model import Device

# NetCon Import:
from inventory.connections.netcon import NetCon
from inventory.connections.apicon import ApiCon

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
    queue = 'collect_data'

    def _run(self, pk, *args, **kwargs):
        # Collect all device objects based on provided pk value:
        collected_objects = self._collect_device_objects(pk)

    def _collect_device_objects(self, pk):
        """
        Collect provided device or devices object.

        Parameters:
        -----------------
        pk: integer, string or list
            int = return one device data collection.
            list = return multiple devices data collection.
            str 'all' = return all active devices data collection.

        Return:
        --------
        Iterable <class 'django.db.models.query.QuerySet'>
        """

        # Declare collected objects variable:
        collected_objects = None

        # (PK: Integer) Collect single device object:
        if isinstance(pk, int):
            collected_objects = self._collect_objects(Device, 'pk', pk)
        
        # (PK: List) Collect provided device objects from list of devices pk integers:
        elif isinstance(pk, list):
            # Check if list contains only integers:
            check_status = True
            for single_pk in pk:
                if not isinstance(single_pk, int):
                    # Log type error:
                    self.logger.debug(
                        f'Provided device PK value is not a integer.',
                        self.task_id, self.corelate_object)
                    check_status = False
            # Collect data if check process passed:
            if check_status:
                collected_objects = self._collect_objects(Device, 'pk__in', pk)
        
        # (PK: String 'All') Collect all devices object:
        elif pk == 'all':
            collected_objects = self._collect_objects(Device, 'all')
        
        # Wrong data type error:
        else:
            # Log type error:
            self.logger.debug(
                f'Provided device PK value is wrong type.',
                self.task_id, self.corelate_object)

        # Return all collected objects:
        return collected_objects

# Task registration:
CheckDeviceStatus = app.register_task(CheckDeviceStatus())
