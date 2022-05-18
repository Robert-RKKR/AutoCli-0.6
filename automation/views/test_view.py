# Django Import:
from django.shortcuts import render

# Application Import:
from logger.logger import Logger

# Task Import:
from automation.task import test_task
from automation.tasks.collect_device_data import collect_device_data

# Logger initialization:
logger = Logger('Page')

def automation(request):

    logger.info('------------------------------------')

    # Collect data to display:
    data = {
        'output': 'Test RKKR',
        'log': '',
    }

    # data['output'] = test_task.delay([True, False])
    data['output'] = collect_device_data(1)
    
    # GET method:
    return render(request, 'basic.html', data)
