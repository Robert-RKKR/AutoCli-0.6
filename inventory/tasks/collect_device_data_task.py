# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.1'

# Base task Import:
from autocli.basetask.basetask import BaseTask

# Models Import:
from inventory.models.device_collected_data_model import DeviceCollectedData
from inventory.models.device_update_model import DeviceUpdate

# Django exception Import:
from django.db import IntegrityError

# NetCon Import:
from inventory.connections.netcon import NetCon

# Celery application Import:
from autocli.celery import app


# Test taks class:
class CollectDeviceDataTask(BaseTask):
    """
    Collect data from specified device or devices, using SSH protocol.
    Usage: CollectDeviceDataTask.delay(<pk value>)

    Parameters:
    -----------------
    pk: integer, string or list
        int = collecting data from one specific device, into data collection model.
        list = collecting data from provided devices, into data collection model.
        str 'all' = collecting data from all devices, into data collection model.
    
    Steps to follow:
    1. Collect all device objects based on provided pk value.
    2. Collect data from devices using SSH protocol.
    3. Create a new Device update object.
    4. Save collected data, into device collected data object.
    celery -A autocli worker -Q collect_data -l INFO
    """

    name = 'Collect device data'
    description = 'Collect data from specified device or devices, using SSH protocol.'
    logger_name = 'Collect device data'
    queue = 'collect_data'

    def _run(self, pk, *args, **kwargs):
        
        # Success counter:
        successful = 0
        # (Step: 1) Collect all device objects based on provided pk value:
        collected_objects = self._collect_device_objects(pk)
        # Verify that the object was collected correctly:
        if collected_objects:
            
            # Collect all operation timer:
            start_operation_timer = self._start_execution_timer()
            
            # Iterate thru all collected device objects:
            for collected_device_object in collected_objects:
                
                # Start single operation clock counter:
                self._start_execution_timer()
                # Update globally accessible variables:
                self.corelate_object = collected_device_object
                self.corelate_object_name = collected_device_object.name
                # (Step: 2) Collect data from devices using SSH protocol:
                collected_data = self._collect_data_from_device(collected_device_object)
                # End clock counter:
                self._end_execution_timer()
                
                # Check if device data has been collected correctly:
                if collected_data:
                    # (Step: 3) Create a new Device update object:
                    update_object = self._create_update_object(collected_device_object)
                    # (Step: 4) Save collected data, into device collected dada object:
                    if update_object:
                        output = self._save_to_device_collected_data(collected_data, update_object)
                        # Check output status:
                        if output:
                            # Raise successes command counter:
                            successful += 1
                        # update device update model status:
                        update_object.status = 1
                        update_object.result_status = True
                        update_object.save(update_fields=['status', 'result_status'])
                    else:
                        # update device update model status:
                        update_object.status = 2
                        update_object.result_status = False
                        update_object.save(update_fields=['status', 'result_status'])
                else:
                    # Create message:
                    message = f'Data could not be collected from device',\
                        f' {self.corelate_object_name} (NR. 37286274758).'
                    # Log data collection error:
                    self.logger.warning(message, self.task_id, self.corelate_object_name, True)
                    # Send message to channel:
                    self.send_message(message, self.queue)
                    # update device update model status:
                    update_object.status = 2
                    update_object.result_status = False
                    update_object.save(update_fields=['status', 'result_status'])

            # Summary of the operations execution:
            end_operation_timer = self._start_execution_timer()
            operation_timer = round(end_operation_timer - start_operation_timer, 5)
            # Create summary message:
            if successful == 1:
                # Create summary data collection process message:
                message = f'Process of collecting information from all requested devices '\
                f'has been accomplish (Successfully collected data from {successful} '\
                f'device out of {len(collected_objects)} requested device, '\
                f'in {operation_timer} seconds).'
            elif successful > 1:
                # Create summary data collection process message:
                message = f'Process of collecting information from all requested devices '\
                f'has been accomplish (Successfully collected data from {successful} '\
                f'devices out of {len(collected_objects)} requested devices, '\
                f'in {operation_timer} seconds).'
            else:
                # Create fails of data collection process message:
                message = f'Process of collecting information from all requested devices fails.' 
            # Log end of process:
            self.logger.info(message, self.task_id, None, True)
            # Send message to channel:
            self.send_message(message, self.queue)

        else:
            # Log data collection error:
            self.logger.warning('An error occurred during attempt to collect provided device/s, based on PK.',
                self.task_id, self.corelate_object_name)
            # Log data collection user error:
            self.logger.warning('An error occurred during data collection (NR. 374527153764).',
                self.task_id, self.corelate_object_name, True)

        # Return successful variable:
        return successful

    def _save_to_device_collected_data(self, collected_data, update_object):
        """
        Save collected data to collect device data object.
        """

        # Defiant counts values:
        commands_count = len(collected_data)
        successes_command = 0

        # Iterate thru all collected commands:
        for single_command_output in collected_data:

            # Collect command data:
            command_name = single_command_output['command']
            command_raw_data = single_command_output['command_output']
            command_processed_data = single_command_output['processed_output']
            # Collect collected data status:
            raw_data_status = self._check_output_status(command_raw_data)
            processed_data_status = self._check_output_status(command_processed_data)
            # Check collected data operation status:
            if processed_data_status and raw_data_status:
                result_status = True
                # Raise successes command counter:
                successes_command += 1
            else:
                result_status = False

            try: # Try to create single device collected data object:
                DeviceCollectedData.objects.create(
                    # Update corelation:
                    device_update=update_object,
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
                # Log fails of data collection process:
                self.logger.warning(
                    f'Process of creating device collected data object fails,'\
                    f' on device {self.corelate_object_name}.\n{error}',
                    self.task_id, self.corelate_object_name)
                # Return False value
                return False
            
        # Create message:
        message = f'Successfully collected {successes_command} output/s '\
        f'outputs from {commands_count} command/s, on device {self.corelate_object_name}. '\
        f'Execution time {self.execution_timer} seconds.'
        # Send message to channel:
        self.send_message(message, self.queue)

        # Log end of collected data saving process:
        if successes_command > 0:
            self.logger.info(
                f'Process of collecting information from {self.corelate_object_name} '\
                f'has been accomplish (Collected {successes_command} '
                f'\outputs from {commands_count} commands). '\
                f'Execution time {self.execution_timer} seconds.',
                self.task_id, self.corelate_object_name, True)
            return True
        else:
            self.logger.warning(
                f'Process of collecting information from '
                f'\{self.corelate_object_name} has failed. '\
                f'Execution time {self.execution_timer} seconds.',
                self.task_id, self.corelate_object_name, True)
            return False


    def _create_update_object(self, collected_device_object):
        """
        Create a new Device update object.
        """

        # Declare update object variable:
        new_update_object = None

        try: # Try to create new update object:
            new_update_object = DeviceUpdate.objects.create(
                device=collected_device_object, status=0)
        except IntegrityError as error:
            self.logger.warning(
                f'Process of creating device update object fails,'\
                f' on device {self.corelate_object_name}.\n{error}',
                self.task_id, self.corelate_object_name)
            # Change update object variable to False:
            new_update_object = False

        # Return new update object:
        return new_update_object

    def _collect_data_from_device(self, collected_device_object):
        """
        Collect data from device using SSH protocol (NetCon class).
        """

        # Declare collected data variable:
        collected_data = None

        # Confect to device using NetCon class:
        connection = NetCon(collected_device_object, self.task_id).open_connection()
        # Check if connection was establish:
        if connection:
            # Collect all data from device:
            collected_data = connection.execute_device_type_templates()
            # Close SSH connection with device:
            connection.close_connection()
        else:
            # Change collect data variable to False:
            collected_data = False

        # Return all collected data:
        return collected_data
        
# Task registration:
CollectDeviceDataTask = app.register_task(CollectDeviceDataTask())
