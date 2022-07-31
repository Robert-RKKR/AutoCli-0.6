# Django Import:
from django.urls import path

# Application Import:
from inventory.views.test_view import automation, logger_page, test_all_devices_view, test_single_devices_view

app_name = 'inventory'

urlpatterns = [
    path('test', automation, name='inventory'),
    path('logger', logger_page, name='logger'),
    path('devices', test_all_devices_view, name='device_all'),
    path('device/<str:pk>', test_single_devices_view, name='device_one'),
]
