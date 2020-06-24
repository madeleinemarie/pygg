from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
    balance = value - arg
    if balance == 0:
        return f"You're exactly on budget. What a coincidence!"
    elif balance < 0:
        return f"You're ${abs(balance)} over your monthly budget. Time to tighten up the belt."
    else:
        return f"You're ${balance} under your budget. Treat yo' self!"
    

