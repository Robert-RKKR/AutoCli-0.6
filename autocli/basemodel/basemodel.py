# Django language import:
from django.utils.translation import gettext_lazy as _

# Django Import:
from django.db import models

# Managers Import:
from .managers import ActiveManager
from .managers import NotDeleted


# Validators Import:
from .validators import DescriptionValueValidator
from .validators import NameValueValidator


# Base models class:
class BaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = _('Model')
        verbose_name_plural = _('Models')

        # Abstract class value:
        abstract = True

    # Model validators:
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()

    # Model data time information:
    created = models.DateTimeField(
        verbose_name=_('Created'),
        help_text=_('Object create date.'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name=_('Updated'),
        help_text=_('Object last update date.'),
        auto_now=True
    )

    # Model status values:
    deleted = models.BooleanField(default=False)
    root = models.BooleanField(
        verbose_name=_('Root'),
        help_text=_('Root object is not deletable.'),
        default=False
    )
    active = models.BooleanField(
        verbose_name=_('Active'),
        help_text=_(f'Status of {Meta.verbose_name} object.'),
        default=True
    )

    # Main model values:
    name = models.CharField(
        verbose_name=_('Name'),
        help_text=_('Xxx.'),
        max_length=32,
        blank=False,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'unique': 'Object with this name already exists.',
            'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.',
        },
    )
    description = models.CharField(
        verbose_name=_('Description'),
        help_text=_('Xxx.'),
        max_length=256, default=f'{Meta.verbose_name} description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
    )

    # Model objects manager:
    objects = NotDeleted()

    # Model representation:
    def __str__(self) -> str:
        return self.name
