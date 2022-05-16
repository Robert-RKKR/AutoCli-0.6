# Django Import:
from django.utils.translation import gettext_lazy as _
from django.db import models

# Base Model Import:
from autocli.basemodel.basemodel import BaseModel


class Template(BaseModel):
    """ Xxx. """

    class Meta:
        
        # Model name values:
        verbose_name = _('Template')
        verbose_name_plural = _('Templates')

    # All main values:
    sfm_expression = models.TextField(
        verbose_name=_('Xxx'),
        help_text=_('Xxx.'),
    )
