# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Django Import:
from django.utils import timezone

# Models Import:
from inventory.models.device_collected_data_model import DeviceCollectedData
from inventory.models.device_update_model import DeviceUpdate
from inventory.models.device_model import Device

# Logger import:
from logger.models.log_model import Log

# Celery Import:
from celery import shared_task
from autocli.celery import app
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Channels variable:
channel_layer = get_channel_layer()


@shared_task(bind=True, track_started=True, name='Log collector')
def collect_last_logs(self) -> bool:

    output_string = ''
    second_ago = timezone.now() - timezone.timedelta(0,1)
    logs = Log.objects.filter(timestamp__gte=second_ago)
    for log in logs:
        output_string = output_string + ' ' + log.message
    
    # Send message to async_to_sync:
    async_to_sync(channel_layer.group_send)('collect', {'type': 'send_collect', 'text': output_string})
