# Django Import:
from django.utils.deconstruct import deconstructible
from django.core import validators


@deconstructible
class HostnameValueValidator(validators.RegexValidator):
    regex = r'^[0-9,A-Z,a-z,-_. ]{4,32}$'
    message = 'The object hostname must contain 4 to 32 digits, letters and special characters -, _, . or spaces.'
    flags = 0
