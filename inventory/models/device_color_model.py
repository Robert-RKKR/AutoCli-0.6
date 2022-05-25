# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Constants Import:
from inventory.constants import COLOR_ICONS


# Credential model:
class DeviceColor(BaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Device color')
        verbose_name_plural = _('Device colors')

    # Main model values:
    ico = models.IntegerField(
        verbose_name=_('Color icon'),
        help_text=_('Color graphical representation.'),
        choices=COLOR_ICONS,
        default=0
    )
