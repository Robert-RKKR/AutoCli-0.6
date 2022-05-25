# Django Import:
from django.urls import path

# Application Import:
from inventory.views.test_view import automation

app_name = 'inventory'

urlpatterns = [
    path('test', automation, name='inventory'),
]
