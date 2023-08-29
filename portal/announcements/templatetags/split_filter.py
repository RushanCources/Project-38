from django import template

register = template.Library()


@register.filter
def split(value):
    return value.split('/')[-1]
