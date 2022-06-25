# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import SimpleBaseModel

# Django user model Import:
from django.contrib.auth.models import User

# Constants declaration:
ACTION = (
    (0, _('---')),
    (1, _('Create')),
    (2, _('Delete')),
    (3, _('Update'))
)

# Device model:
class Change(SimpleBaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Change')
        verbose_name_plural = _('Changes')

    
    # Corelation witch user model:
    administrator = models.ForeignKey(
        User,
        verbose_name=_('Administrator'),
        help_text=_('Administrator responsible for change.'),
        on_delete=models.SET_NULL,
        null=True
    )

    # Action:
    action = models.IntegerField(
        verbose_name=_('Change action'),
        help_text=_('Change action.'),
        choices=ACTION,
        default=0
    )

    # Change object details:
    model_name = models.CharField(
        verbose_name=_('Command name'),
        help_text=_('CLI command name.'),
        max_length=64
    )
    object_name = models.CharField(
        verbose_name=_('Command name'),
        help_text=_('CLI command name.'),
        max_length=64
    )

    # Change details:
    before = models.JSONField(
        verbose_name=_('Command name'),
        help_text=_('CLI command name.'),
        max_length=64,
        null=True,
        blank=True
    )
    after = models.JSONField(
        verbose_name=_('Command raw data'),
        help_text=_('CLI command raw data output.'),
        null=True,
        blank=True
    )
