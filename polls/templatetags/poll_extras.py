from django import template

register = template.Library()

@register.filter
def div(value, arg):
    """나눗셈 필터"""
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def mul(value, arg):
    """곱셈 필터"""
    try:
        return float(value) * float(arg)
    except ValueError:
        return 0 