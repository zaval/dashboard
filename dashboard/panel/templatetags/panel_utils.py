from datetime import datetime
from django import template

register = template.Library()


@register.filter()
def to_float(value):

    return float(value)


@register.filter()
def diff_days(value, fmt):
    d = datetime.strptime(value, fmt)
    n = datetime.now()
    return (d - n).days
