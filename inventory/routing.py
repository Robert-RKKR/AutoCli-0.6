# Django Import:
from django.urls import path

# Application Import:
from .consumers import CollectDataConsumer
from .consumers import CollectConsumer
from .consumers import LoggerConsumer
from .consumers import StatusConsumer

ws_urlpatterns = [
    path('ws/collect/', CollectConsumer.as_asgi()),
    path('ws/logger/', LoggerConsumer.as_asgi()),
    path('ws/collect_data/', CollectDataConsumer.as_asgi()),
    path('ws/status_update/', StatusConsumer.as_asgi()),
]