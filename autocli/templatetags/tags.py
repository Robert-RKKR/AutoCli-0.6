# Django Import:
from django import template

# Register template:
register = template.Library()

# Filters:
@register.filter
def language_url(request):
    return request.path[3:]
