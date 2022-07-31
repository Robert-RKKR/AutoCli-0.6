# Django Import:
from django.shortcuts import render
import threading

# Application Import:
from logger.logger import Logger
from django.db import IntegrityError

# Task Import:
from inventory.models.device_type_template_model import DeviceTypeTemplate
from inventory.tasks.old.collect_device_data import collect_device_data, collect_all_devices_data
from inventory.connections.netcon import NetCon
from inventory.connections.apicon import ApiCon
from inventory.tasks.collect_device_data_task import CollectDeviceDataTask
from inventory.tasks.check_device_status_task import CheckDeviceStatus
from inventory.models.device_collected_data_model import DeviceCollectedData
from inventory.models.device_update_model import DeviceUpdate
from inventory.models.device_model import Device

from django.core.exceptions import ValidationError

# Logger initialization:
logger = Logger('Page')

def test_all_devices_view(request):
    data = {
        'output': 'All devices view',
    }

    devices = Device.objects.all()

    data['devices'] = devices
    return render(request, 'test_all_devices_view.html', data)

def test_single_devices_view(request, pk):
    data = {
        'output': 'Single device view',
    }

    devices = Device.objects.all()
    data['devices'] = devices
    device = Device.objects.get(pk=pk)
    data['device'] = device
    data['output'] = device.name

    updates = DeviceUpdate.objects.filter(device=device)
    data['updates'] = updates
    last_update = DeviceUpdate.objects.filter(device=device).latest('updated')
    data['last_update'] = last_update

    all_collected_data = DeviceCollectedData.objects.filter(device_update=last_update)
    data['all_collected_data'] = all_collected_data

    return render(request, 'test_single_devices_view.html', data)

def logger_page(request):
    data = {
        'output': 'Log page',
        'log': '',
    }

    device = Device.objects.get(pk=1)


    # data['output'] = CollectDeviceDataTask.delay(1)

    # device = Device.objects.get(pk=1)
    # connection = ApiCon(device)
    # url = 'restconf/data/Cisco-IOS-XE-native:native/hostname'
    # data['output'] = connection.get(url)

    # logger.info('aaa')
    # logger.info('bbb')
    # logger.info('ccc')
    # logger.info('ddd')
    # logger.info('eee')
    return render(request, 'test.html', data)


def check_device_activity(device):
    ssh_connection = NetCon(device, repeat_connection=1).test_connection()
    if ssh_connection:
        device.ssh_status = True
    else:
        device.ssh_status = False
    device.save(update_fields=['ssh_status'])



def automation(request):

    # Collect data to display:
    data = {
        'output': 'Test RKKR',
        'log': '',
    }
    logger.info('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    data['output'] = CollectDeviceDataTask.delay('all')
    # data['output'] = CheckDeviceStatus.delay('all')
    


    
    
    # output = []
    # threads = list()
    # devices = Device.objects.filter(active=True)
    
    # for device in devices:
    #     thread = threading.Thread(target=check_device_activity, args=(device,))
    #     threads.append(thread)
    #     thread.start()

    # for index, thread in enumerate(threads):
    #     thread.join()
        
    # data['output'] = output







    # data['output'] = collect_all_devices_data.delay()
    # data['output'] = collect_last_logs.delay()

    # data['output'] = test_task.delay([True, False])
    # data['output'] = collect_device_data(1)

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
    return render(request, 'test.html', data)
