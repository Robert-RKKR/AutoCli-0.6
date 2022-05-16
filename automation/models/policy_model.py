# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Scheduler Import:
from django_celery_beat.models import IntervalSchedule

# Models Import:
from automation.models.template_model import Template
from inventory.models.device_model import Device
from inventory.models.folder_model import Folder


# Policy model:
class Policy(BaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Policy')
        verbose_name_plural = _('Polices')

    # Corelation witch scheduler model:
    scheduler = models.ForeignKey(
        IntervalSchedule,
        verbose_name=_('Xxx'),
        help_text=_('Xxx.'),
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # Relationships with other models:
    devices = models.ManyToManyField(
        Device,
        verbose_name=_('Xxx'),
        help_text=_('Xxx.'),
        blank=True
    )
    folders = models.ManyToManyField(
        Folder,
        verbose_name=_('Xxx'),
        help_text=_('Xxx.'),
        blank=True
    )
    templates = models.ManyToManyField(
        Template,
        verbose_name=_('Xxx'),
        help_text=_('Xxx.'),
        blank=True
    )
