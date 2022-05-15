# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Other models Import:
from inventory.models.credential_model import Credential

# Validators Import:
from inventory.validators import HostnameValueValidator

# Constants Import:
from inventory.constants import DEVICETYPES
from inventory.constants import DEVICE_ICONS



# Device model:
class Device(BaseModel):
    """ 
        Devices is the main component of the AutoCli application,
        it contains basic network Information about devices that
        are not collected directly from the devices themselves.
    """

    class Meta:
        
        # Model name values:
        verbose_name = _('Device')
        verbose_name_plural = _('Devices')

    # Validators:
    hostname_validator = HostnameValueValidator()

    # Device status:
    ssh_status = models.BooleanField(
        verbose_name=_('SSH status'),
        help_text=_('Status of SSH connection to the device.'),
        default=False
    )
    https_status = models.BooleanField(
        verbose_name=_('HTTPS status'),
        help_text=_('Status of HTTPS connection to the device.'),
        default=False
    )

    # Main model values:
    hostname = models.CharField(
        verbose_name=_('Hostname'),
        help_text=_('Valid IP address or domain name.'),
        max_length=32,
        blank=False,
        unique=True,
        validators=[hostname_validator],
        error_messages={
            'null': _('IP / DNS name field is mandatory.'),
            'blank': _('IP / DNS name field is mandatory.'),
            'unique': _('Device with this hostname already exists.'),
            'invalid': _('Enter a valid IP address or DNS resolvable hostname. It must contain 4 to 32 digits, letters and special characters -, _, . or spaces.'),
        },
    )
    device_type = models.IntegerField(
        verbose_name=_('Device type'),
        help_text=_('Type of network device system.'),
        choices=DEVICETYPES,
        default=0
    )
    ico = models.IntegerField(
        verbose_name=_('Device Icon'),
        help_text=_('Network device graphic representation.'),
        choices=DEVICE_ICONS,
        default=0
    )
    ssh_port = models.IntegerField(
        verbose_name=_('SSH port'),
        help_text=_('SSH protocol port number.'),
        default=22
    )
    https_port = models.IntegerField(
        verbose_name=_('HTTPS port'),
        help_text=_('HTTPS protocol port number.'),
        default=443
    )

    # Security and credentials:
    credential = models.ForeignKey(
        Credential,
        verbose_name=_('Credential'),
        help_text=_('Credential needed to establish SSH / HTTPS connection.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    secret = models.CharField(
        verbose_name=_('Secret'),
        help_text=_('Network device secret password.'),
        max_length=64,
        null=True,
        blank=True
    )
    token = models.CharField(
        verbose_name=_('API token'),
        help_text=_('Network device API key.'),
        max_length=128,
        null=True,
        blank=True
    )
    certificate = models.BooleanField(
        verbose_name=_('Certificate'),
        help_text=_('Check network device certificate during HTTPS connection.'),
        default=False
    )
