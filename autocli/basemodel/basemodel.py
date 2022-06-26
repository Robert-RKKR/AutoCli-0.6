# Django language import:
from django.utils.translation import gettext_lazy as _

# Django Import:
from django.db import models

# Simple base model Import:
from .simplebasemodel import SimpleBaseModel

# Import change model:
from changes.models.change_model import Change

# Managers Import:
from .managers import ChangeLogManager

# Validators Import:
from .validators import DescriptionValueValidator
from .validators import NameValueValidator


# Base models class:
class BaseModel(SimpleBaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Model')
        verbose_name_plural = _('Models')

        # Abstract class value:
        abstract = True

    # Model validators:
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()
    
    # Class name value:
    class_name = Meta.verbose_name

    # Model status values:
    root = models.BooleanField(
        verbose_name=_('Root'),
        help_text=_(f'{class_name} with root option cannot be deleted.'),
        default=False
    )
    active = models.BooleanField(
        verbose_name=_('Active'),
        help_text=_(f'Status of {class_name} object.'),
        default=True
    )

    # Main model values:
    name = models.CharField(
        verbose_name=_('Name'),
        help_text=_(f'{class_name} name.'),
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
        help_text=_(f'{class_name} description.'),
        max_length=256,
        default=f'{class_name} description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
    )

    # Model objects manager:
    objects = ChangeLogManager()

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.name}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.name}'

    # def save(self, *args, **kwargs):
        
    #     # Create change model:
    #     change = Change.objects.create(
    #         action=3,
    #         model_name=self.class_name,
    #         object_name=self.name
    #     )
    #     # Inherit from save method:
    #     super().save(*args, **kwargs)


# class ObjectCustomManager(object):
    
#     def __init__(self, model):
#         self.model = model
      
#     def __enter__(self):
#         # Create change model:
#         change = Change.objects.create(
#             action=3,
#             model_name=self.model.Meta.verbose_name,
#             object_name=
#         )
  
#     def __exit__(self):
        
