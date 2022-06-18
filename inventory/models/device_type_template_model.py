# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Other models Import:
from inventory.models.device_type_model import DeviceType

# Constants declaration:
TYPE = (
    (0, _('Undefined')),
    (1, _('Command template')),
    (2, _('API template'))
)

class DeviceTypeTemplate(BaseModel):
    """
    CLI command template can be processed to receive CLI configurations commands.
    A TextFSM string or Regex expression can then be used to check that the received output is correct.
    """

    class Meta:
        
        # Model name values:
        verbose_name = _('Device type template')
        verbose_name_plural = _('Device type templates')

    # Device type corelation:
    device_type = models.ForeignKey(
        DeviceType,
        verbose_name=_('Device type'),
        help_text=_('Type of network device system.'),
        on_delete=models.CASCADE,
    )

    # Device template type:
    template_type = models.IntegerField(
        verbose_name=_('Template type'),
        help_text=_('Device template type.'),
        choices=TYPE,
        default=0
    )

    # SSH commands values:
    command = models.CharField(
        verbose_name=_('CLI command'),
        help_text=_('CLI command that will be executed on network device.'),
        max_length=32,
        null=True,
        blank=True
    )
    sfm_expression = models.TextField(
        verbose_name=_('SFM expression'),
        help_text=_('SFM expression used to check if CLI command/s output is correct.'),
        null=True,
        blank=True
    )

    # HTTPS Api values:
    url = models.CharField(
        verbose_name=_('API URL'),
        help_text=_('URL required to collect API response from device.'),
        max_length=256,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = [['command', 'device_type']]
