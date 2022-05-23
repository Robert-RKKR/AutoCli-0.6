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
    device_type = models.IntegerField(
        verbose_name=_('Device type'),
        help_text=_('Supported device type.'),
        choices=DEVICE_TYPE,
        default=0
    )
    ico = models.IntegerField(
        verbose_name=_('Device type icon'),
        help_text=_('Device type graphical representation.'),
        choices=DEVICE_TYPE_ICONS,
        default=0
    )
