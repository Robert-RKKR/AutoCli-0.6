# Django Import:
import random
import time

# Celery application Import:
from autocli.celery import app

# Base task Import:
from autocli.basetask.basetask import BaseTask

# Application Import:
from logger.logger import Logger

from celery._state import _task_stack

# Test taks class:
class TestTask(BaseTask):

    name = 'RKKR fun'
    description = 'RKKR fun description.'
    logger_name = 'Fun task'

    def _run(self, pk, *args, **kwargs):
        # pk = random.randrange(100)
        time.sleep(2)
        message = f'RKKR - Class candent test taks. Test pk data = {pk}'
        self.logger.critical(message, self.request.id)
        # Send message:
        self.send_message(message, 'collect')
        
# Task registration:
TestTask = app.register_task(TestTask())
