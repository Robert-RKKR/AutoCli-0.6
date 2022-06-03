# Django Import:
from django.urls import path

# Application Import:
from .consumers import CollectConsumer
from .consumers import LoggerConsumer

ws_urlpatterns = [
    path('ws/collect/', CollectConsumer.as_asgi()),
    path('ws/logger/', LoggerConsumer.as_asgi()),
]