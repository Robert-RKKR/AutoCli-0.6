# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import SimpleBaseModel

# Other models Import:
from automation.models.device_update_model import DeviceUpdate


# Device model:
class DeviceCollectedData(SimpleBaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Device collected data')
        verbose_name_plural = _('Device collected data')

    
    # Corelation witch device model:
    update = models.ForeignKey(
        DeviceUpdate,
        verbose_name=_('Update model'),
        help_text=_('Corelated update model.'),
        on_delete=models.CASCADE
    )

    # Status values:
    result_status = models.BooleanField(
        verbose_name=_('Result status'),
        help_text=_('A positive result means that command updates was collected.'),
        default=False
    )

    # Main model values:
    command_name = models.CharField(
        verbose_name=_('Command name'),
        help_text=_('CLI command name.'),
        max_length=64
    )
    command_raw_data = models.TextField(
        verbose_name=_('Command raw data'),
        help_text=_('CLI command raw data output.'),
        null=True,
        blank=True
    )
    command_processed_data = models.JSONField(
        verbose_name=_('Command processed data'),
        help_text=_('CLI command FSM proccess data.'),
        null=True,
        blank=True
    )
