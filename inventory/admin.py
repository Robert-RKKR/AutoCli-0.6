# Django Import:
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

# Base Admin Import:
from autocli.baseadmin.baseadmin import BaseAdmin

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


@admin.register(Device)
class DeviceAdmin(BaseAdmin):

    list_display = (
        'name', 'active', 'hostname', 'ssh_status', 'https_status', 'credential', 'device_type',
    )
    list_filter = (
        'active', 'device_type', 'ssh_status', 'https_status', 'color',
    )
    search_fields = (
        'name', 'hostname',
    )
    list_select_related = (
        'credential', 'device_type',
    )
    readonly_fields = (
        'root', 'ssh_status', 'https_status',
    )
    fieldsets = (
        (_('Basic settings'), {
            'classes': ('wide', 'extrapretty',),
            'fields': ('name', 'hostname', 'description',)
        }),
        (_('Device status'), {
            'classes': ('wide', 'extrapretty',),
            'fields': ('root', 'active', 'ssh_status', 'https_status',)
        }),
        (_('Additional settings',), {
            'classes': ('collapse',),
            'fields': ('device_type', 'ico', 'color', 'ssh_port', 'https_port',),
        }),
        (_('Security and credentials'), {
            'classes': ('collapse',),
            'fields': ('credential', 'secret', 'token', 'certificate',),
        }),
    )


@admin.register(DeviceGroup)
class DeviceGroupAdmin(BaseAdmin):

    list_display = (
        'name', 'active', 'color', 'root_folder', 'credential',
    )
    list_filter = (
        'active', 'credential', 'root_folder', 'color',
    )
    search_fields = (
        'name',
    )
    fieldsets = (
        (_('Basic settings'), {
            'classes': ('wide', 'extrapretty',),
            'fields': ('name', 'ico', 'color', 'description',)
        }),
        (_('Group status'), {
            'classes': ('wide', 'extrapretty',),
            'fields': ('root', 'active',)
        }),
        (_('Items',), {
            'classes': ('wide', 'extrapretty',),
            'fields': ('devices', 'credential', 'root_folder',),
        }),
    )


@admin.register(DeviceTypeTemplate)
class DeviceTypeTemplateAdmin(BaseAdmin):

    list_display = (
        'name', 'active', 'template_type',
    )
    list_filter = (
        'active', 'template_type',
    )
    search_fields = (
        'name',
    )
    fieldsets = (
        (_('Basic settings'), {
            'classes': ('wide', 'extrapretty',),
            'fields': ('name', 'description', 'template_type',)
        }),
        (_('Device template status'), {
            'classes': ('wide', 'extrapretty',),
            'fields': ('root', 'active',)
        }),
        (_('SSH collect settings',), {
            'classes': ('collapse',),
            'fields': ('command', 'sfm_expression',),
        }),
        (_('HTTPS collect settings',), {
            'classes': ('collapse',),
            'fields': ('url',),
        }),
    )


@admin.register(DeviceCollectedData)
class DeviceCollectedDataAdmin(admin.ModelAdmin):

    exclude = ('deleted',)
    empty_value_display = '-None-'
    readonly_fields = (
        'device_update', 'result_status', 'raw_data_status', 'processed_data_status',
        'command_name', 'command_raw_data', 'command_processed_data',
    )
    list_display = (
        'pk', 'device_update', 'result_status', 'raw_data_status', 'processed_data_status',
    )
    list_filter = (
        'result_status', 'raw_data_status', 'processed_data_status',
    )
    search_fields = (
        'device_update',
    )
    ordering = ('-pk',)


@admin.register(DeviceCredential)
class DeviceCredentialAdmin(BaseAdmin):

    list_display = (
        'name', 'active', 'username',
    )
    list_filter = (
        'active', 'color',
    )
    search_fields = (
        'name', 'username',
    )
    fieldsets = (
        (_('Basic user information'), {
            'classes': ('wide', 'extrapretty',),
            'fields': ('name', 'username', 'ico', 'color',)
        }),
        (_('Credential status'), {
            'classes': ('wide', 'extrapretty',),
            'fields': ('root', 'active',)
        }),
        (_('Security',), {
            'classes': ('collapse',),
            'fields': ('password',),
        }),
    )

# Register your models here:
admin.site.register(DeviceColor)
admin.site.register(DeviceType)
admin.site.register(DeviceUpdate)
admin.site.register(Policy)
admin.site.register(PolicyRunner)
admin.site.register(PolicyTask)
admin.site.register(PolicyTemplate)
