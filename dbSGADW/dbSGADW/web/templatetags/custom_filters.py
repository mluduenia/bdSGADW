from django import template
import re

register = template.Library()

@register.filter
def extraer_numero(value):
    match = re.search(r'S(\d+)_0', value)
    return match.group(1) if match else value