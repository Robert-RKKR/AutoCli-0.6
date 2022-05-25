# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import SimpleBaseModel

# Models Import:
from inventory.models.policy_model import Policy

# Constants declaration:
STATUS = (
    (0, _('Initiation')),
    (1, _('Collecting data')),
    (2, _('Saved data'))
)


# Policy runner model:
class PolicyRunner(SimpleBaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Policy runner')
        verbose_name_plural = _('Policy runner')

    # Corelation with policy model:
    policy = models.ForeignKey(
        Policy,
        verbose_name=_('Policy'),
        help_text=_('Corelated policy.'),
        on_delete=models.CASCADE
    )

    # Status values:
    status = models.IntegerField(
        verbose_name=_('Update status'),
        help_text=_('Policy runner status.'),
        choices=STATUS,
        default=0
    )
    result_status = models.BooleanField(
        verbose_name=_('Result status'),
        help_text=_('A positive result means that all of the commands output match TextFSM and Regex expression.'),
        default=False
    )
