# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Models Import:
from inventory.models.device_type_template_model import DeviceTypeTemplate


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
        max_length=32
    )
    napalm_name = models.CharField(
        verbose_name=_('Napalm name'),
        help_text=_('Napalm name.'),
        max_length=32
    )

    # Corelation witch device type template:
    device_type_templates = models.ManyToManyField(
        DeviceTypeTemplate,
        verbose_name=_('Device type template/s'),
        help_text=_('All devices type templates.'),
        blank=True
    )
