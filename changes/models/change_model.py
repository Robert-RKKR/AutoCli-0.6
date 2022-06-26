# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

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
class Change(models.Model):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Change')
        verbose_name_plural = _('Changes')

    # Model data time information:
    created = models.DateTimeField(
        verbose_name=_('Created'),
        help_text=_('Change create date.'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_('Change last update date.'),
        auto_now=True
    )
    
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

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.object_name}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.object_name}'
