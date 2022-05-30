# Celery Import:
from celery import Task


class MyTask(Task):

    def run(self, source, *args, **kwargs):
        return 'RKKR'
