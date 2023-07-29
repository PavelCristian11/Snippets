from django import template

register = template.Library()

@register.filter(name="replace_str")
def replace_str(value):
    """Removes all values of arg from the given string"""
    return value.replace(" ", "_")