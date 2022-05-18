# Django Import:
from django.contrib import admin

# Models Imports:
from automation.models.device_update_model import DeviceUpdate
from automation.models.policy_model import Policy
from automation.models.policy_runner_model import PolicyRunner
from automation.models.policy_task_model import PolicyTask
from automation.models.template_model import Template

# Register your models here.
admin.site.register(DeviceUpdate)
admin.site.register(Policy)
admin.site.register(PolicyRunner)
admin.site.register(PolicyTask)
admin.site.register(Template)
