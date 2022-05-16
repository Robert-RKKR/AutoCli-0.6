# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import SimpleBaseModel

# Models Import:
from automation.models.policy_model import Policy

# Constants declaration:
STATUS = (
    (0, _('Initiation')),
    (1, _('Collecting data')),
    (2, _('Saved data'))
)


# Policy manager model:
class PolicyManager(SimpleBaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Policy manager')
        verbose_name_plural = _('Policy managers')

    # Corelation witch policy model:
    policy = models.ForeignKey(
        Policy,
        verbose_name=_('Xxx'),
        help_text=_('Xxx.'),
        on_delete=models.CASCADE
    )

    # Policy manager status declaration:
    status = models.IntegerField(
        verbose_name=_('Update status'),
        help_text=_('Policy manager status.'),
        choices=STATUS,
        default=0
    )

    # 
    result = models.JSONField(
        verbose_name=_('Xxx'),
        help_text=_('Xxx.'),
        blank=True,
        null=True
    )
    tasks_ids = models.JSONField(
        verbose_name=_('Xxx'),
        help_text=_('Xxx.'),
        blank=True,
        null=True
    )
