from django import template
import urllib.parse

register = template.Library()


@register.filter
def split(value):
    return value.split('/')[-1]


@register.filter
def encode(value):
    return urllib.parse.unquote(value)
