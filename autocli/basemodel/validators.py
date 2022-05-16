# Django Import:
from django.utils.deconstruct import deconstructible
from django.core import validators


# Validators class:
@deconstructible
class NameValueValidator(validators.RegexValidator):
    regex = r'^[0-9,A-Z,a-z,-_ ]{3,32}$'
    message = 'The object name must contain 3 to 32 digits, letters and special characters -, _ or spaces.'
    flags = 0


@deconstructible
class DescriptionValueValidator(validators.RegexValidator):
    regex = r'^[0-9,A-Z,a-z,-_. ]{8,256}$'
    message = 'Description must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'
    flags = 0
