from django.template import Library


register = Library()


@register.filter(is_safe=True)
def run(func):
    return func