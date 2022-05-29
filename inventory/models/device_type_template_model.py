# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Other models Import:
from inventory.models.device_type_model import DeviceType


class DeviceTypeTemplate(BaseModel):
    """
    CLI command template can be processed to receive CLI configurations commands.
    A TextFSM string or Regex expression can then be used to check that the received output is correct.
    """

    class Meta:
        
        # Model name values:
        verbose_name = _('Device type template')
        verbose_name_plural = _('Device type templates')

    # All main values:
    command = models.CharField(
        verbose_name=_('CLI command'),
        help_text=_('CLI command that will be executed on network device.'),
        max_length=32,
        unique=True
    )
    sfm_expression = models.TextField(
        verbose_name=_('SFM expression'),
        help_text=_('SFM expression used to check if CLI command/s output is correct.')
    )
    # Device type corelation:

    device_type = models.ForeignKey(
        DeviceType,
        verbose_name=_('Device type'),
        help_text=_('Type of network device system.'),
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = [['command', 'device_type']]
