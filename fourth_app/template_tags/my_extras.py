from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This will cut out all the values by this!
    """
    return value.replace(arg, '')
