# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel


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
    command = models.TextField(
        verbose_name=_('CLI template'),
        help_text=_('CLI command/s template.'),
        null=True,
        blank=True
    )
    sfm_expression = models.TextField(
        verbose_name=_('SFM expression'),
        help_text=_('SFM expression used to check if CLI command/s output is correct.'),
        null=True,
        blank=True
    )
