# Django Import:
from django.shortcuts import render

# Application Import:
from logger.logger import Logger

# Task Import:
from automation.tasks import test_task

# Logger initialization:
logger = Logger('Page')

def automation(request):

    logger.info('Hello, welcome on RKKR page :)')

    # Collect data to display:
    data = {
        'output': 'Test RKKR',
        'log': '',
    }

    data['output'] = test_task.delay()
    
    # GET method:
    return render(request, 'basic.html', data)
