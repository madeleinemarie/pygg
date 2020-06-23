from django import template
from django.utils import timezone
import datetime

register = template.Library()

@register.filter(name='daysuntil', expects_localtime=True)
def days_until(target_date):
    today = datetime.date.today()
    if isinstance(target_date, datetime.date):
        delta = target_date - today
    else:
        delta = target_date.date() - today
    if delta.days > 1:
        return f"Due in {delta.days} days"
    elif delta.days == 1:
        return 'Due tomorrow'
    elif delta.days == 0:
        return 'Due today'
    else:
        return 'Overdue'

@register.filter(name='daysstyle')
def days_style(target_date):
    today = datetime.date.today()
    if isinstance(target_date, datetime.date):
        delta = target_date - today
    else:
        delta = target_date.date() - today
    if delta.days > 1:
        return 'due-later'
    elif delta.days == 1:
        return 'due-tomorrow'
    elif delta.days == 0:
        return 'due-today'
    else:
        return 'overdue'


@register.filter(name='justdays', expects_localtime=True)
def just_days(target_date):
    today = datetime.date.today()
    if isinstance(target_date, datetime.date):
        delta = target_date - today
    else:
        delta = target_date.date() - today
    if delta.days > 1:
        return f"{delta.days} days"
    elif delta.days == 1:
        return 'Tomorrow'
    elif delta.days == 0:
        return 'Today'
    else:
        return 'Overdue'

