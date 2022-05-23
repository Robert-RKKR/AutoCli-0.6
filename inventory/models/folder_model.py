# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel

# Models Import:
from inventory.models.credential_model import Credential
from inventory.models.device_model import Device
from inventory.models.color_model import Color

# Constants Import:
from inventory.constants import FOLDER_ICONS
from inventory.constants import COLOR_ICONS


# Folder model:
class Folder(BaseModel):
    """ Folders allow you to group network devices. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Folder')
        verbose_name_plural = _('Folders')

    # All main values:
    ico = models.IntegerField(
        verbose_name=_('Folder icon'),
        help_text=_('Folder graphic representation.'),
        choices=FOLDER_ICONS,
        default=0
    )

    # Corelation witch color model:
    color = models.ForeignKey(
        Color,
        verbose_name=_('Color'),
        help_text=_('Corelated color.'),
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # Corelation witch other folder model:
    root_folder = models.ForeignKey(
        'self',
        verbose_name=_('Root folder'),
        help_text=_('The parent folder to witch the current folder belongs.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    # Corelation witch device model:
    devices = models.ManyToManyField(
        Device,
        verbose_name=_('Devices'),
        help_text=_('All devices that belongs to current folder.'),
        blank=True
    )

    # Defaults values:
    credential = models.ForeignKey(
        Credential,
        verbose_name=_('Default credential'),
        help_text=_('Folder default credential needed to establish SSH / HTTPS connection.'),
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
