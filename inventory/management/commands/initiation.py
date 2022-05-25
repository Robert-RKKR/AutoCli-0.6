# Django Import:
from django.core.management.base import BaseCommand, CommandError

# Yaml reader import:
from inventory.yaml_reader import yaml_read

# Model Import:
from inventory.models.device_type_model import DeviceType
from inventory.models.device_model import Device

# Constant Import:
from inventory.constants import DEVICE_TYPE_INIT_PATH


# Command class:
class Command(BaseCommand):

    help = 'Xxx.'

    def handle(self, *args, **options):
        
        device_type_init_list = yaml_read(f'{DEVICE_TYPE_INIT_PATH}/device_type_init.yml')['output']
        for row in device_type_init_list:
            new_device_type = DeviceType.objects.create(**row)
