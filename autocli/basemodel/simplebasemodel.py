# Django language import:
from django.utils.translation import gettext_lazy as _

# Django Import:
from django.db import models

# Managers Import:
from .managers import BasicManager


# Base models class:
class SimpleBaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = _('Model')
        verbose_name_plural = _('Models')

        # Abstract class value:
        abstract = True

    # Class name value:
    class_name = Meta.verbose_name

    # Model data time information:
    created = models.DateTimeField(
        verbose_name=_('Created'),
        help_text=_(f'{class_name} create date.'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_(f'{class_name} last update date.'),
        auto_now=True
    )

    # Model status values:
    deleted = models.BooleanField(default=False)
    
    # Model objects manager:
    objects = BasicManager()

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.created}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.created}'
