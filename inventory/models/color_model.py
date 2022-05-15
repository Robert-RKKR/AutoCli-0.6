# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Validators Import:
from inventory.validators import ColorValueValidator

# Other models Import:
from inventory.models.credential_model import Credential
from inventory.models.device_model import Device
from inventory.models.folder_model import Folder


# Color model:
class Color(BaseModel):
    """ 
        The Color model is working like Tag,
        its available to be added to all device,
        group and credential models.
    """

    class Meta:
        
        # Model name values:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    # Validators:
    color_validator = ColorValueValidator()

    # Main model values:
    hexadecimal = models.CharField(
        verbose_name=_('Color'),
        help_text=_('Color hexadecimal value.'),
        unique=True,
        max_length=7,
        validators=[color_validator],
        error_messages={
            'null': _('Colour field is mandatory.'),
            'blank': _('Colour field is mandatory.'),
            'unique': _('Color with this hexadecimal value already exists.'),
            'invalid': _('Enter the correct colour value. It must be a 3/6 hexadecimal number with # character on begining.'),
        },
    )

    # Relationships with other models:
    devices = models.ManyToManyField(
        Device,
        verbose_name=_('Devices'),
        help_text=_('All devices that belongs to current color.'),
        blank=True
    )
    folders = models.ManyToManyField(
        Folder,
        verbose_name=_('Folders'),
        help_text=_('All folder that belongs to current color.'),
        blank=True
    )
    credentials = models.ManyToManyField(
        Credential,
        verbose_name=_('Credentials'),
        help_text=_('All credentials that belongs to current color.'),
        blank=True
    )
    ico = 'hexadecimal'
