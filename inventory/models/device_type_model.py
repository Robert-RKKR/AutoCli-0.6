# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Constants Import:
from automation.connections.device_types import DEVICE_TYPE
from inventory.constants import DEVICE_TYPE_ICONS


# Credential model:
class DeviceType(BaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Device type')
        verbose_name_plural = _('Device types')

    # Main model values:
    netmiko_name = models.CharField(
        verbose_name=_('Netmiko name'),
        help_text=_('Netmiko name.'),
        max_length=32,
        null=True,
        blank=True
    )
    napalm_name = models.CharField(
        verbose_name=_('Napalm name'),
        help_text=_('Napalm name.'),
        max_length=32,
        null=True,
        blank=True
    )
    ico = models.IntegerField(
        verbose_name=_('Device type icon'),
        help_text=_('Device type graphical representation.'),
        choices=DEVICE_TYPE_ICONS,
        default=0
    )
