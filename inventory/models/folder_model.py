# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Other models Import:
from inventory.models.credential_model import Credential
from inventory.models.device_model import Device

# Constants Import:
from inventory.constants import FOLDER_ICONS


# Folder model:
class Folder(BaseModel):
    """ Folders allow you to group network devices. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Folder')
        verbose_name_plural = _('Folders')

    # All defaults main values:
    ico = models.IntegerField(
        verbose_name=_('Default device Icon'),
        help_text=_('Folder default network device graphic representation.'),
        choices=FOLDER_ICONS,
        default=0
    )
    ssh_port = models.IntegerField(
        verbose_name=_('Default SSH port'),
        help_text=_('Folder default SSH protocol port number.'),
        default=22
    )
    https_port = models.IntegerField(
        verbose_name=_('Default HTTPS port'),
        help_text=_('Folder default HTTPS protocol port number.'),
        default=443
    )

    # All defaults security and credentials:
    credential = models.ForeignKey(
        Credential,
        verbose_name=_('Default credential'),
        help_text=_('Folder default credential needed to establish SSH / HTTPS connection.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    secret = models.CharField(
        verbose_name=_('Default secret'),
        help_text=_('Folder default network device secret password.'),
        max_length=64,
        null=True,
        blank=True
    )
    certificate = models.BooleanField(
        verbose_name=_('Default certificate'),
        help_text=_('Folder default certificate check status.'),
        default=False
    )

    # Relationships with other models:
    root_folder = models.ForeignKey(
        'self',
        verbose_name=_('Root folder'),
        help_text=_('The parent folder to witch the current folder belongs.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    devices = models.ManyToManyField(
        Device,
        verbose_name=_('Devices'),
        help_text=_('All devices that belongs to current folder.'),
        blank=True
    )
