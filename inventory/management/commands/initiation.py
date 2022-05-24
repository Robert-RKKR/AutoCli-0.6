# Django Import:
from django.core.management.base import BaseCommand, CommandError

# Model Import:
from inventory.models.device_model import Device


# Command class:
class Command(BaseCommand):

    help = 'Xxx.'

    def handle(self, *args, **options):
        print('RKKR test')
