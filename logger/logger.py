# Document descryption:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Model Import:
from .models.log_model import Log

# Severity constants declaration:
DEBUG = 5
INFO = 4
WARNING = 3
ERROR = 2
CRITICAL = 1

# Main Logger class:
class Logger:
    """
    Logger class.
    
    Attributes:
    -----------------
    application:
        Xxx.
    user_message:
        Xxx.

    Methods:
    --------
    critical:
        Xxx.
    error:
        Xxx.
    warning:
        Xxx.
    info:
        Xxx.
    debug:
        Xxx.
    """

    def __init__(self, application: str = 'NoName', user_message: bool = False) -> None:
        """ Log application acclivity. """

        # Verify if the application variable is a valid sting:
        if isinstance(application, str):
            self.application = application
        else:
            raise TypeError('The provided application variable must be string.')
        
        # Verify if the user message variable is a valid boolean:
        if isinstance(user_message, bool):
            self.user_message = user_message
        else:
            raise TypeError('The provided user message variable must be boolean.')

    def critical(self, message: str, task_id: str = None, correlated_object: str = None, **kwarg) -> Log:
        """
        Create a new log based on the following data:

        Parameters:
        -----------------
        message: string
            Logging message string value.
        task_id: string
            Celery task ID.
        correlated_object: object
            Object of device or other model that is supported.
        """

        # Run process of log and details log creation:
        return self._run(CRITICAL, message, task_id, correlated_object)

    def error(self, message: str, task_id: str = None, correlated_object: str = None, **kwarg) -> Log:
        """
        Create a new log based on the following data:

        Parameters:
        -----------------
        message: string
            Logging message string value.
        task_id: string
            Celery task ID.
        correlated_object: object
            Object of device or other model that is supported.
        """
        
        # Run process of log and details log creation:
        return self._run(ERROR, message, task_id, correlated_object)

    def warning(self, message: str, task_id: str = None, correlated_object: str = None, **kwarg) -> Log:
        """
        Create a new log based on the following data:

        Parameters:
        -----------------
        message: string
            Logging message string value.
        task_id: string
            Celery task ID.
        correlated_object: object
            Object of device or other model that is supported.
        """

        # Run process of log and details log creation:
        return self._run(WARNING, message, task_id, correlated_object)

    def info(self, message: str, task_id: str = None, correlated_object: str = None, **kwarg) -> Log:
        """
        Create a new log based on the following data:

        Parameters:
        -----------------
        message: string
            Logging message string value.
        task_id: string
            Celery task ID.
        correlated_object: object
            Object of device or other model that is supported.
        """

        # Run process of log and details log creation:
        return self._run(INFO, message, task_id, correlated_object)

    def debug(self, message: str, task_id: str = None, correlated_object: str = None, **kwarg) -> Log:
        """
        Create a new log based on the following data:

        Parameters:
        -----------------
        message: string
            Logging message string value.
        task_id: string
            Celery task ID.
        correlated_object: object
            Object of device or other model that is supported.
        """

        # Run process of log and details log creation:
        return self._run(DEBUG, message, task_id, correlated_object)

    def _run(self, severity, message, task_id, correlated_object):
        """ Run process of log and details log creation. """

        # Check provided data:
        # if isinstance(message, str) is False:
        #     raise TypeError('The provided message variable must be string.')
        # if isinstance(task_id, str) is False and task_id is not None:
        #     raise TypeError('The provided task id variable must be string.')
        # if isinstance(correlated_object, str) is False and correlated_object is not None:
        #     raise TypeError('The provided correlated object variable must be string.')

        # Create new log based on provided data:
        log = self._create_log(severity, message, task_id, correlated_object)

        # return log:
        return log

    def _create_log(self, severity, message, task_id, correlated_object):
        """ Create new log in Database """

        # Define new log:
        new_log = None

        # Collect all log data:
        log_data = {
            'correlated_object': correlated_object,
            'user_message': self.user_message,
            'application': self.application,
            'severity': severity,
            'message': message,
            'task_id': task_id,
        }

        try: # Tyr to create a new log:
            # Create a new log:
            new_log = Log.objects.create(**log_data)
        except:
            # If there was a problem during log creation process, return False:
            return False
        else:
            # Return created log object:
            return new_log
