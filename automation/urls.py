# Django Import:
from django.urls import path

# Application Import:
from .views.test_view import automation

app_name = 'automation'

urlpatterns = [
    path('test', automation, name='automation'),
]
