# Django Import:
from django.shortcuts import render

# Application Import:
from logger.logger import Logger
from django.db import IntegrityError

# Task Import:
from inventory.models.device_type_template_model import DeviceTypeTemplate
from inventory.tasks.collect_device_data import collect_device_data, collect_all_devices_data
from inventory.connections.netcon import NetCon
from inventory.task import test_task

# Models Import:
from inventory.models.device_collected_data_model import DeviceCollectedData
from inventory.models.device_model import Device

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
    # data['output'] = collect_device_data(1)

    # data['output'] = collect_all_devices_data()
    data['output'] = collect_device_data(1)
    # try:
    #     data['output'] = Device.objects.get(pk=1)
    # except IntegrityError as error:
    #     data['output'] = error

    # device = Device.objects.get(pk=1)
    # connection = NetCon(device).open_connection()
    # # data['output'] = connection.enabled_commands(['show version', 'show interfaces', 'show interfaces switchport', 'show ip interface', 'show cdp neighbors', 'show clock', 'show access-list', 'show ip access-list', 'show ip route', 'show inventory', 'show vrf'])
    # if connection:
    #     # data['output'] = connection.enabled_commands(['show access-list', 'show ip access-list'])
    #     # template = DeviceTypeTemplate.objects.get(pk=1)
    #     # data['output'] = connection.enabled_commands(fsm_template_object=template)
    #     # data['output'] = collect_device_data(1)
    #     # data['output'] = connection.execute_device_type_templates()
    #     connection.close_connection()
    
    # GET method:
    return render(request, 'basic.html', data)
