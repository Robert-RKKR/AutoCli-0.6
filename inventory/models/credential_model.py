# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Constants Import:
from inventory.constants import USER_ICONS
from inventory.constants import COLOR_ICONS


# Credential model:
class Credential(BaseModel):
    """ 
        The Credential specifies the login information (Login, password)
        needed in the login process when connecting to network devices.
    """

    class Meta:
        
        # Model name values:
        verbose_name = _('Credential')
        verbose_name_plural = _('Credentials')

    # Main model values:
    username = models.CharField(
        verbose_name=_('Username'),
        help_text=_('Local / remote user name.'),
        max_length=64,
        error_messages={
            'null': _('Username field is mandatory.'),
            'blank': _('Username field is mandatory.'),
            'invalid': _('Enter the correct username value.'),
        },
    )
    password = models.CharField(
        verbose_name=_('Password'),
        help_text=_('Local / remote user password.'),
        max_length=64,
        null=True,
        blank=True
    )
    ico = models.IntegerField(
        verbose_name=_('Credential icon'),
        help_text=_('Credential graphical representation.'),
        choices=USER_ICONS,
        default=0
    )
    color = models.IntegerField(
        verbose_name=_('Color'),
        help_text=_('Color graphic representation.'),
        choices=COLOR_ICONS,
        default=0
    )
