# Django Import:
from django.contrib import admin

# Models Imports:
from inventory.models.device_collected_data_model import DeviceCollectedData
from inventory.models.device_type_model import DeviceType
from inventory.models.credential_model import Credential
from inventory.models.device_model import Device
from inventory.models.folder_model import Folder
from inventory.models.color_model import Color

# Register your models here:
admin.site.register(DeviceCollectedData)
admin.site.register(DeviceType)
admin.site.register(Credential)
admin.site.register(Device)
admin.site.register(Folder)
admin.site.register(Color)
