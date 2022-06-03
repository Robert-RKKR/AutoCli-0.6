# Django Import:
from django.urls import path

# Application Import:
from inventory.views.test_view import automation, logger_page

app_name = 'inventory'

urlpatterns = [
    path('test', automation, name='inventory'),
    path('logger', logger_page, name='logger'),
]
