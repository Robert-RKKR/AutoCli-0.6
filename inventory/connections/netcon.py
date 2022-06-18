# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '2.2'

# Python Import:
import textfsm
import io

# Netmiko Import:
from netmiko.ssh_exception import  AuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_autodetect import SSHDetect
from netmiko import ConnectHandler
from paramiko import ssh_exception

# Other models Import:
from inventory.models.device_type_template_model import DeviceTypeTemplate
from inventory.models.device_type_model import DeviceType

# Connection Import:
from .connection import Connection

# Logger import:
from logger.logger import Logger

# Constance Import:
from inventory.constants import COMMANDS

# Logger class initiation:
logger = Logger('SSH Netconf connection')


# Main NetCon class:
class NetCon(Connection):
    """
    The NetCon class uses netmiko library, to establish a SSH connection with networks device.

    Methods:
    --------
    update_device_type:
        Collect device type via SSH protocol and updates device type attributes of device object.
    close_connection:
        Close SSH connection.
    enabled_commands:
        Executes commands that do not require privileged mode.
    configuration_commands:
        Executes commands that require privileged mode.
    execute_device_type_template:
        Xxx.
    execute_device_type_templates:
        Xxx.
    """

    def open_connection(self):
        """ Open a new SSH connection """

        # Check if device need autodetect process:
        if self.supported_device is None:
            logger.debug(
                f'Device type of device: {self.device_name}, must be discovered.',
                self.task_id, self.device_name)
            # Update device type based on information collected via SSH protocol:
            self.update_device_type()
            # Connect to network device:
            self._ssh_connect()
        # Check connection status:
        elif not self.connection_status:
            self._ssh_connect()

        # Start connection timer if connected successfully:
        if self.connection_status:
            logger.info(
                f'SSH connection to device: {self.device_name}, has been established.',
                self.task_id, self.device_name)
            # Start session timer:
            self._start_connection_timer()
            return self
        else:
            return False
    
    def close_connection(self):
        """ End of SSH connection """

        # Check connection status:
        if self.connection_status:
            # Close SSH connection:
            self.connection.disconnect()
            # Log close of SSH connection:
            logger.debug('SSH session ended.', self.task_id, self.device_name)
            # End session timer:
            self._end_connection_timer(logger)

    def update_device_type(self):
        """ Obtain network device type information using SSH protocol. And update Device type object. """

        # Log beginning of network device type checking process:
        logger.debug(
            f'Started acquiring information about the type '\
            f'of device: {self.device_name}:{self.device_hostname}.',
            self.task_id, self.device_name)

        # Connect to device to check device type, using SSH protocol:
        discovered_device_type_name = self._ssh_connect(autodetect=True)

        if discovered_device_type_name:

            try: # Collecting device type object:
                device_type_object = DeviceType.objects.get(netmiko_name=discovered_device_type_name) 
            except:
                logger.warning(
                    f'Device type {discovered_device_type_name} running '\
                    f'on device: {self.device_name}, is not supported.',
                    self.task_id, self.device_name)
                # Change supported value to unsupported:
                self.supported_device = False
                try: # Try to collect unsupported device type:
                    device_type_object = DeviceType.objects.get(pk=99)
                except:
                    logger.critical(
                        'Could not collect Unsupported device type.',
                        self.task_id, self.device_name)
            else:
                # Log successful device type collection:
                logger.info(
                    f'Device: {self.device_name}:{self.device_hostname} '\
                    f'is running {device_type_object.name} software.',
                    self.task_id, self.device_name)
                # Change supported value to supported:
                self.supported_device = True
                # Change current device type to new one:
                self.device.device_type = device_type_object
                self.device_type = device_type_object

                try: # Try to update device type object:
                    self.device.save() 
                except: # Return exception if there is a problem during the update of the device type object:
                    logger.debug(
                        f'Exception occurs, durning device type update '\
                        f'process (device: {self.device_name}:{self.device_hostname}).',
                        self.task_id, self.device_name)
                    # Return collected device type name:
                    return discovered_device_type_name
                else:
                    logger.debug(
                        f'Device type of device: {self.device_name}:'\
                        f'{self.device_hostname} has been updated.',
                        self.task_id, self.device_name)
                
    def enabled_commands(self, commands: str or list = False, expect_string: str = False, fsm_template_object = False) -> str or list:
        """
        Retrieves a string or list containing network CLI commands, and sends them to a network device using SSH protocol.
        ! Usable only with enable levels commend/s.
        
        Parameters:
        -----------------
        commands: String
            Provided device object, to establish a SSH connection.
        commands: List
            Provided device object, to establish a SSH connection.
        expect_string: String
            Specifies the Celery task ID value, that will be added to logs messages.
        fsm_template_object: DeviceTypeTemplate object
            Xxx.

        Return:
        --------
        String containing command/s output.
        """

        # Check if provided command variable is valid string or list:
        if isinstance(commands, str) or isinstance(commands, list) or commands is False:
            pass
        else:
            # Raise exception:
            raise TypeError('The provided command/s variable must be a string or list.')
            
        # Check if provided expect string variable is valid string:
        if isinstance(expect_string, str) or expect_string is False:
            pass
        else:
            # Raise exception:
            raise TypeError('The provided expect string variable must be a string.')

        # Check connection status:
        if self.connection_status:

            # Start clock count:
            start_time = self._start_execution_timer()
            # Collect data from device:
            return_data = {}

            if fsm_template_object:
                command = fsm_template_object.command
                return_data[commands] = self._enabled_command_execution(
                    fsm_template_object=fsm_template_object,
                    command=command
                )

            else:
                # First option: command is string:
                if isinstance(commands, str):
                    # Save command execution output to dictionary:
                    return_data[commands] = self._enabled_command_execution(commands, expect_string)
                elif isinstance(commands, list) or isinstance(commands, tuple):
                    for command in commands:
                        # Second option: command is list / tuple of strings:
                        if isinstance(command, str):
                            # Save command execution output to dictionary:
                            return_data[command] = self._enabled_command_execution(command)
                        # Third option: command is list / tuple of lists or tuples:
                        elif isinstance(command, list) or isinstance(command, tuple):
                            # Save command execution output to dictionary:
                            return_data[command] = self._enabled_command_execution(command[0], command[1])
                        else:
                            # Raise exception:
                            raise TypeError('Wrong data type.')

            # Finish clock count & method execution time:
            self._end_execution_timer(start_time, logger, commands)
            # Return data:
            return return_data

        else:
            # Inform that the command cannot be sent:
            logger.debug(
                f'Command/s could not be executed because SSH '\
                f'connection with device: {self.device_name}:'\
                f'{self.device_hostname}, was interrupted.',
                self.task_id, self.device_name)

    def configuration_commands(self, commands: str or list) -> str:
        """
        Retrieves a string or list containing network CLI commands, and sends them to a network device using SSH protocol.
        ! Usable only with configuration terminal levels commends.
        
        Parameters:
        -----------------
        commands: String
            Provided device object, to establish a SSH connection.
        commands: List
            Provided device object, to establish a SSH connection.

        Return:
        --------
        String containing command/s output.
        """

        # Check if provided command variable is valid string or list:
        if isinstance(commands, str) or isinstance(commands, list):
            pass
        else:
            # Raise exception:
            raise TypeError('The provided command/s variable must be a string or list.')

        # Check connection status:
        if self.connection_status:

            # Start clock count:
            start_time = self._start_execution_timer()

            # Collect data from device:
            return_data = self._config_command_execution(commands)

            # Finish clock count & method execution time:
            self._end_execution_timer(start_time, logger, commands)

            # Return data:
            return return_data

        else:
            # Inform that the command cannot be sent:
            logger.debug(
                f'Command/s could not be executed because SSH connection '\
                f'with device: {self.device_name}:{self.device_hostname}, was interrupted.',
                self.task_id, self.device_name)

    def execute_device_type_template(self, fsm_template_object = False) -> list:
        """
        """
        return self._enabled_command_execution(
            command=fsm_template_object.command,
            fsm_template_object=fsm_template_object
        )

    def execute_device_type_templates(self) -> list:
        """
        """
        output = []
        # Collect all device type templates:
        all_device_type_templates = DeviceTypeTemplate.objects.filter(
            device_type=self.device_type,
            template_type=1
        )
        
        for device_type_templates in all_device_type_templates:
            output.append(self.execute_device_type_template(device_type_templates))
        return output

    def _ssh_connect(self, autodetect: bool = False) -> str:
        """ 
        Connect to device using SSH protocol.
        Returns the type of network device.
        """

        # Check if device is supported before connection attempt:
        if self.supported_device is False:

            if not autodetect:
                logger.debug(
                    f'device: {self.device_name}:{self.device_hostname}, is not supported.',
                    self.task_id, self.device_name)

        elif self.supported_device or autodetect:

            # Performs a specified number of SSH connection attempts to a specified device.
            for connection_attempts in range(1, self.repeat_connection + 1):

                # Sleep before second and rest of conception attempts:
                if connection_attempts > 1:
                    self._sleep()

                # Log stat of a new SSH connection attempt:
                logger.debug(
                    f'SSH connection to device: {self.device_name}:{self.device_hostname}, '\
                    f'has been started (Attempt: {connection_attempts}).',
                    self.task_id, self.device_name)

                try: # Try connect to device, using SSH protocol:
                    # Check if the device type must be detected automatically:
                    if autodetect:
                        # Connect to device to check device type, using SSH protocol:
                        self.connection = SSHDetect(**{
                            'device_type': 'autodetect',
                            'host': self.device_hostname,
                            'port': self.device_ssh_port,
                            'username': self.device_username,
                            'password': self.device_password})
                    else:
                        # Connect to device, using SSH protocol:
                        self.connection = ConnectHandler(**{
                            'device_type': self.device_type.netmiko_name,
                            'host': self.device_hostname,
                            'port': self.device_ssh_port,
                            'username': self.device_username,
                            'password': self.device_password})

                # Handel SSH connection exceptions:
                except AuthenticationException as error:
                    logger.debug(
                        f'Error occurred during SSH connection to device:'\
                        f' {self.device_name}:{self.device_hostname}\n{error}',
                        self.task_id, self.device_name)
                    # Change connection status to False.
                    self.connection_status = False
                    # Log warning error on last attempt:
                    if connection_attempts == self.repeat_connection:
                        logger.warning(
                            f'Application was unable to establish SSH connection '\
                            f'to device: {self.device_name}, (Authentication error).',
                            self.task_id, self.device_name)
                        # Return False:
                        return False
                except NetMikoTimeoutException as error:
                    logger.debug(
                        f'Error occurred during SSH connection to device: '\
                        f'{self.device_name}:{self.device_hostname}\n{error}',
                        self.task_id, self.device_name)
                    # Change connection status to False.
                    self.connection_status = False
                    # Log warning error on last attempt:
                    if connection_attempts == self.repeat_connection:
                        logger.warning(
                            f'Application was unable to establish SSH connection '\
                            f'to device: {self.device_name}, (Connection timeout).',
                            self.task_id, self.device_name)
                        # Return False:
                        return False
                except ssh_exception.SSHException as error:
                    logger.debug(
                        f'Error occurred during SSH connection to device: '\
                        f'{self.device_name}:{self.device_hostname}\n{error}',
                        self.task_id, self.device_name)
                    # Change connection status to False.
                    self.connection_status = False
                    # Log warning error on last attempt:
                    if connection_attempts == self.repeat_connection:
                        logger.warning(
                            f'Application was unable to establish SSH connection '\
                            f'to device: {self.device_name}, (SSH exception).',
                            self.task_id, self.device_name)
                        # Return False:
                        return False
                except OSError as error:
                    logger.critical(error, self.task_id, self.device_name)
                    # Change connection status to False.
                    self.connection_status = False
                    # Return connection straus:
                    return self.connection_status
                except TypeError as error:
                    logger.critical(error, self.task_id, self.device_name)
                    # Change connection status to False.
                    self.connection_status = False
                    # Return connection straus:
                    return self.connection_status
                except ValueError as error:
                    logger.critical(error, self.task_id, self.device_name)
                    # Change connection status to False.
                    self.connection_status = False
                    # Return connection straus:
                    return self.connection_status

                else:
                    # Change connection status to True.
                    self.connection_status = True
                    # Log the start of a new connection:
                    logger.debug(
                        f'SSH connection to device: {self.device_name}:{self.device_hostname}, '\
                        f'has been established (Attempt: {connection_attempts}).',
                        self.task_id, self.device_name)

                    if autodetect:    
                        # Collect information about device type:
                        device_type = self.connection.autodetect()
                        self.connection_status = False
                        self.connection = False
                        return device_type
                    else: # Return connection:
                        return self.connection

            return self.connection_status

    def _config_command_execution(self, command: str) -> str:
        """ Configuration CLI command execution. """

        # Log start of command execution: 
        logger.debug(
            f'Sending of a new configuration CLI command "{command}" to '\
            f'device: {self.device_name}:{self.device_hostname}, has been started.',
            self.task_id, self.device_name)

        try:
            return_data = self.connection.send_config_set(command)

        except UnboundLocalError as error:
            # Log debug message for support:
            logger.debug(
                f'Error occurred during CLI operation on device: '\
                f'{self.device_name}:{self.device_hostname}\n{error}',
                self.task_id, self.device_name)
            # Log informational message for user:
            logger.warning(
                f'Application was unable to send config commands to device: '\
                f'{self.device_name}.',
                self.task_id, self.device_name)
            # Changed return data to False:
            return False
        except OSError as error:
            # Log critical message for support:
            logger.critical(error, self.task_id, self.device_name)
            # Log informational message for user:
            logger.warning(
                f'Execution of command/s "{command}" on device: '\
                f'{self.device_name}, was interrupted.',
                self.task_id, self.device_name)
            # Changed return data to False:
            return False
        except TypeError as error:
            # Log critical message for support:
            logger.critical(error, self.task_id, self.device_name)
            # Log informational message for user:
            logger.warning(
                f'Execution of command/s "{command}" on device: '\
                f'{self.device_name}, was interrupted.',
                self.task_id, self.device_name)
            # Changed return data to False:
            return False

        else:
            if return_data:
                # Log end of command execution:
                logger.debug(
                    f'The configuration CLI command "{command}" has '\
                    f'been sent to device: {self.device_name}:{self.device_hostname}.',
                    self.task_id, self.device_name)
            else:
                # Log end of command execution:
                logger.debug(
                    f'The configuration CLI command "{command}" has '\
                    f'been sent to device: {self.device_name}:{self.device_hostname}. Nut return no data.',
                    self.task_id, self.device_name)

            # Log executions of CLI command/s:
            logger.info(
                f'Command/s "{command}" was executed on device {self.device_name}.',
                self.task_id, self.device_name)
            # Return command output:
            return return_data

    def _enabled_command_execution(self, command: str, expect_string: str = False, fsm_template_object = False) -> str:
        """ Enabled CLI command execution. """

        # Log start of command execution: 
        logger.debug(
            f'Sending of a new enabled CLI command "{command}" has '\
            f'been started on device: {self.device_name}:{self.device_hostname}.',
            self.task_id, self.device_name)
        
        # Prepare return data:
        return_data = {
            'command': command,
            'expect_string': expect_string,
            'command_output': None,
            'processed_output': None,
            'error': None
        }

        try: # Try to execute provided CLI command:
            if expect_string is False:
                command_output = self.connection.send_command(
                    command_string=command)
            else:
                command_output = self.connection.send_command(
                    command_string=command,
                    expect_string=expect_string)

        except UnboundLocalError as error:
            # Log debug message for support:
            logger.debug(
                f'Error occurred during CLI operation on device: '\
                f'{self.device_name}:{self.device_hostname}\n{error}',
                self.task_id, self.device_name)
            # Log informational message for user:
            logger.warning(
                f'Application was unable to send config commands '\
                f'to device: {self.device_name}.',
                self.task_id, self.device_name)
            # Add error to return data:
            return_data['command_output'] = False
            return_data['error'] = error
            # Changed return data to False:
            return False
        except OSError as error:
            # Log critical message for support:
            logger.critical(error, self.task_id, self.device_name)
            # Log informational message for user:
            logger.warning(
                f'Execution of command "{command}" on device: '\
                f'{self.device_name}, was interrupted.',
                self.task_id, self.device_name)
            # Add error to return data:
            return_data['command_output'] = False
            return_data['error'] = error
            # Changed return data to False:
            return False
        except TypeError as error:
            # Log critical message for support:
            logger.critical(error, self.task_id, self.device_name)
            # Log informational message for user:
            logger.warning(
                f'Execution of command "{command}" on device: '\
                f'{self.device_name}, was interrupted.',
                self.task_id, self.device_name)
            # Add error to return data:
            return_data['command_output'] = False
            return_data['error'] = error
            # Changed return data to False:
            return False

        else:
            # Log end of command execution:
            logger.debug(
                f'CLI command "{command}" has been sent to '\
                f'{self.device_name}:{self.device_hostname}.',
                self.task_id, self.device_name)

            # Check if received output is valid:
            if 'Invalid input detected' in command_output:
                return_data['command_output'] = False
                return_data['error'] = 'Provided command is not valid'
            else:
                # Add command output to return dictionary:
                return_data['command_output'] = command_output
                # Process output data to dictionary:
                processed_data = self._process_command_output_to_dictionary(command, command_output, fsm_template_object)
                return_data['processed_output'] = processed_data

                if processed_data:
                    # Log executions of CLI enabled command:
                    logger.info(
                        f'Enabled command "{command}" was executed and processed successfully.',
                        self.task_id, self.device_name)
            
            # Return data:
            return return_data

    def _process_command_output_to_dictionary(self, command, command_output, fsm_template_object):
        """ Convert commands output to dictionary based on Text FSM templates. """

        logger.debug(
            f'SFM process on command "{command}" collected from device: '\
            f'{self.device_name}:{self.device_hostname}, has been started.',
            self.task_id, self.device_name)

        # FSM result list:
        fsm_result = []
        try: # Try to Collect fsm template:
            if fsm_template_object:
                if not isinstance(fsm_template_object, DeviceTypeTemplate):
                    raise 'FSM template object is wrong type.'
            else:
                fsm_template_object = DeviceTypeTemplate.objects.get(command=command, device_type=self.device_type)
        except:
            return False
        else:
            # Collect data from template object:
            fsm_template = fsm_template_object.sfm_expression
            template_as_file = io.StringIO(fsm_template)
            try: # Try to parse collected data from Text FSM:
                fsm = textfsm.TextFSM(template_as_file)
                result = fsm.ParseText(command_output)
                # Create one or many dict from Text FSM result:
                for value in result:
                    fsm_result.append(dict(zip(fsm.header, value)))
            except textfsm.TextFSMTemplateError as error:
                # Log error during Text FSM process:
                logger.debug(
                    f'Error occurred during SFM operation on device: '\
                    f'{self.device_name}:{self.device_hostname}\n{error}',
                    self.task_id, self.device_name)
                logger.error(
                    f'Text FSM return device template ({fsm_template_object.name}) error.\n{error}',
                    self.task_id, self.device_name)
                # Return False value:
                return False
            except textfsm.TextFSMError as error:
                # Log error during Text FSM process:
                logger.debug(
                    f'Error occurred during SFM operation on device: '\
                    f'{self.device_name}:{self.device_hostname}\n{error}',
                    self.task_id, self.device_name)
                # Return False value:
                return False
            else:
                logger.debug(
                    f'SFM process on command "{command}" collected from '\
                    f'device: {self.device_name}:{self.device_hostname}, has been accomplish.',
                    self.task_id, self.device_name)
                # Return FSM process output:
                return fsm_result
