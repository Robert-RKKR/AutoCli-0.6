# Python Import:
import time

# Celery Import:
from celery import shared_task
from autocli.celery import app
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Channels variable:
channel_layer = get_channel_layer()

@shared_task(bind=True, track_started=True, name='Test task')
def test_task(self) -> bool:
    
    output = f'RKKR {self.request.id}'

    time.sleep(2)

    async_to_sync(channel_layer.group_send)('collect', {'type': 'send_collect', 'text': str(output)})
    return output
