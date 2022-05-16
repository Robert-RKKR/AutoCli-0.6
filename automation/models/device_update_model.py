# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import SimpleBaseModel

# Models Import:
from inventory.models.device_model import Device

# Constants declaration:
STATUS = (
    (0, _('Initiation')),
    (1, _('Collecting data')),
    (2, _('Saved data'))
)


# Device update model:
class DeviceUpdate(SimpleBaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Device update')
        verbose_name_plural = _('Device updates')

    # All main values:
    status = models.IntegerField(
        verbose_name=_('Update status'),
        help_text=_('Device update status.'),
        choices=STATUS,
        default=0
    )
