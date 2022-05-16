# Django Import:
from django.contrib import admin

# Models Imports:
from inventory.models.credential_model import Credential
from inventory.models.device_model import Device
from inventory.models.folder_model import Folder

# Register your models here.
admin.site.register(Credential)
admin.site.register(Device)
admin.site.register(Folder)
