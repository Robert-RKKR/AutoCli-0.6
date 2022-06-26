# Django Import
from django.contrib import admin

@admin.action(description='Change status to active')
def change_status_to_true(modeladmin, request, queryset):
    queryset.update(active=True)

@admin.action(description='Change status to passive')
def change_status_to_false(modeladmin, request, queryset):
    queryset.update(active=False)

class BaseAdmin(admin.ModelAdmin):

    exclude = ('deleted',)
    empty_value_display = '-None-'
    list_display_links = ('name',)
    ordering = ('name',)
    readonly_fields = ('root',)
    list_per_page = 10
    list_max_show_all = 100
    actions = [
        change_status_to_true,
        change_status_to_false
    ]
