# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Celery Import:
from celery import Task

# Channels Import and declaration:
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Python Import:
import time

# Application Import:
from logger.logger import Logger

# Models Import:
from inventory.models.device_model import Device


# Base task class
class BaseTask(Task):

    # Basic celery attributes:
    ignore_result = False
    validation_class = ''
    public = True
    task_id = 'None'

    # Correlated object data:
    corelate_object = None
    corelate_object_name = None

    # Task identity attributes:
    description = ''
    name = 'default'
    queue = 'rkkr'

    # Define logger name:
    logger_name = 'BaseTask'

    # Channels registration:
    channel_layer = get_channel_layer()

    # Timer:
    execution_timer = None

    def run(self, *args, **kwargs):
        # Logger initialization:
        self.logger = Logger(self.logger_name)
        # Collect process ID:
        self.task_id = self.request.id
        # Run task in delay:
        self._run(*args, **kwargs)

    def send_message(self, message: str, channel: str, severity: int = None):
        # Send message to async_to_sync:
        async_to_sync(self.channel_layer.group_send)(channel, {'type': 'send_collect', 'message': message, 'severity': severity})

    def _run(self, *args, **kwargs):
        return True

    def _start_execution_timer(self):
        """ Start task execution time counting. """

        # Start clock count:
        self.execution_timer = time.perf_counter()
        # Return execution timer value:
        return self.execution_timer

    def _end_execution_timer(self):
        """ End task execution time counting. """

        # Finish clock count & method execution time:
        finish_time = time.perf_counter()
        self.execution_timer = round(finish_time - self.execution_timer, 5)

        # Log time of SSH session:
        self.logger.debug(
            f'The execution time of task {self.name} took {self.execution_timer} seconds.',
            self.task_id, self.corelate_object_name)
        # Return execution timer value:
        return self.execution_timer

    def _collect_objects(self, object: object, filter: str, expression: str = None):
        """
        Collect object or objects from database.

        Parameters:
        -----------------
        object: class
            Django model class.
        filter: string
            Django model class parameter.
            If provided filter value is 'all' will return all objects.
        expression: string / none
            Django model class parameter search value.

        Return:
        --------
        Iterable <class 'django.db.models.query.QuerySet'>
        """

        # Declare collected objects variable:
        collected_objects = None

        # Collect all object from provided model:
        if filter == 'all':
            try: # Try to collect all objects from database:
                collected_objects = object.objects.all()
            except:
                # Log error during object collection:
                self.logger.debug(
                    f'Error occurs during object collection.'\
                    f'\nFilter value: {filter}\n'\
                    f'Expression value: {expression}',
                    self.task_id, self.corelate_object_name)
                # Change collect variable to False:
                collected_objects = False

        # Collect filtered object from provided model:
        elif filter and expression:
            # Define filter dictionary:
            filter_variable = {
                filter: expression
            }
            try: # Try to collect object or objects from database:
                collected_objects = object.objects.filter(**filter_variable)
            except:
                # Log error during object collection:
                self.logger.debug(
                    f'Error occurs during object collection.'\
                    f'\nFilter value: {filter}\n'\
                    f'Expression value: {expression}',
                    self.task_id, self.corelate_object_name)
                # Change collect objects variable to False:
                collected_objects = False
                
        # Return all collected objects:
        return collected_objects

    def _check_output_status(self, output):
        if output == {} or output == [] or output is None or output is False:
            return False
        else:
            return True

    def _collect_device_objects(self, pk):
        """
        Collect provided device or devices object.

        Parameters:
        -----------------
        pk: integer, string or list
            int = collecting data from one specific device, into data collection model.
            list = collecting data from provided devices, into data collection model.
            str 'all' = collecting data from all devices, into data collection model.

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
                    self.logger.error(
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
            self.logger.error(
                f'Provided device PK value is wrong type.',
                self.task_id, self.corelate_object)

        # Return all collected objects:
        return collected_objects
