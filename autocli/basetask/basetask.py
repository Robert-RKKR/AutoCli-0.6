# Celery Import:
from celery import Task

# Celery application Import:
from autocli.celery import app

# Channels Import and declaration:
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Application Import:
from logger.logger import Logger


# Base task class
class BaseTask(Task):

    ignore_result = False
    validation_class = ''
    name = ''
    description = ''
    public = True
    channel_layer = get_channel_layer()
    queue = 'rkkr'

    # Define logger name:
    logger_name = 'BaseTask'

    def run(self, *args, **kwargs):
        # Logger initialization:
        self.logger = Logger(self.logger_name)
        # Run task in delay:
        self._run(*args, **kwargs)

    def send_message(self, message: str, channel: str):
        # Send message to async_to_sync:
        async_to_sync(self.channel_layer.group_send)(channel, {'type': 'send_collect', 'text': message})

    def _run(self, *args, **kwargs):
        return True