# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Scheduler Import:
from django_celery_beat.models import IntervalSchedule

# Models Import:
from inventory.models.policy_template_model import PolicyTemplate
from inventory.models.device_group_model import DeviceGroup
from inventory.models.device_model import Device


# Policy model:
class Policy(BaseModel):
    """ Policy model is used by task like source of information to run policy manager task. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Policy')
        verbose_name_plural = _('Polices')

    # Corelation witch scheduler model:
    scheduler = models.ForeignKey(
        IntervalSchedule,
        verbose_name=_('Scheduler'),
        help_text=_('Task scheduler.'),
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # Relationships with other models:
    devices = models.ManyToManyField(
        Device,
        verbose_name=_('Corelated device/s'),
        help_text=_('Xxx.'),
        blank=True
    )
    folders = models.ManyToManyField(
        DeviceGroup,
        verbose_name=_('Corelated group/s'),
        help_text=_('Xxx.'),
        blank=True
    )
    templates = models.ManyToManyField(
        PolicyTemplate,
        verbose_name=_('Corelated template/s'),
        help_text=_('Xxx.'),
        blank=True
    )
