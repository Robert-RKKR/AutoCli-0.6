# Django Import:
from django.urls import path

# Application Import:
from .consumers import CollectConsumer

ws_urlpatterns = [
    path('ws/collect/', CollectConsumer.as_asgi()),
]