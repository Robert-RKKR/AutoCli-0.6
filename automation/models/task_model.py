# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import SimpleBaseModel

# Models Import:


# Task model:
class Task(SimpleBaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
