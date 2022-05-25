# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import SimpleBaseModel

# Models Import:


# Task model:
class PolicyTask(SimpleBaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Policy task')
        verbose_name_plural = _('Policy tasks')

    # Result status value:
    result_status = models.BooleanField(
        verbose_name=_('Result status'),
        help_text=_('A positive result means that the command output match TextFSM and Regex expression.'),
        default=False
    )

    # Status values:
    result_status = models.BooleanField(
        verbose_name=_('Result status'),
        help_text=_('A positive result means that the commands output match TextFSM and Regex expression.'),
        default=False
    )
