from django import template

register = template.Library()

@register.filter(name='crop_first_letter')
def crop_first_letter(value):
    if isinstance(value, str) and len(value) > 0:
        return value[:1]
    return value
