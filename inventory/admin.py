# Django Import:
from django.contrib import admin

# Models Imports:
from inventory.models.device_collected_data_model import DeviceCollectedData
from inventory.models.device_type_model import DeviceType
from inventory.models.device_credential_model import DeviceCredential
from inventory.models.device_model import Device
from inventory.models.device_group_model import DeviceGroup
from inventory.models.device_color_model import DeviceColor
from inventory.models.policy_model import Policy
from inventory.models.policy_runner_model import PolicyRunner
from inventory.models.policy_task_model import PolicyTask
from inventory.models.device_type_template_model import DeviceTypeTemplate
from inventory.models.policy_template_model import PolicyTemplate
from inventory.models.device_update_model import DeviceUpdate

@admin.register(DeviceCollectedData)
class LogAdmin(admin.ModelAdmin):

    empty_value_display = '-None-'
    list_display = (
        'pk', 'device_update', 'result_status', 'raw_data_status', 'processed_data_status',
    )
    list_filter = (
        'result_status', 'raw_data_status', 'processed_data_status',
    )
    search_fields = (
        'device_update',
    )
    ordering = (
        '-pk',
    )

# Register your models here:
admin.site.register(DeviceCredential)
admin.site.register(DeviceGroup)
admin.site.register(DeviceColor)
admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(DeviceUpdate)
admin.site.register(Policy)
admin.site.register(PolicyRunner)
admin.site.register(PolicyTask)
admin.site.register(DeviceTypeTemplate)
admin.site.register(PolicyTemplate)
