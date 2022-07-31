# Django Import:
from django.contrib import admin

# Models Imports:
from .models.log_model import Log


# Admin classes:
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):

    empty_value_display = '-None-'
    list_display = (
        'pk', 'timestamp', 'user_message', 'severity', 'task_id', 'correlated_object', 'application', 'message',
    )
    list_filter = (
        'severity', 'application', 'user_message',
    )
    search_fields = (
        'timestamp', 'message', 'task_id',
    )
    ordering = (
        '-pk',
    )
    readonly_fields = (
        'timestamp', 'severity', 'task_id', 'correlated_object', 'application', 'message', 'user_message',
    )
