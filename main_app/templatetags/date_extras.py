from django import template
from django.utils import timezone
import datetime
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='daysbadge', expects_localtime=True)
def days_until(target_date):
    today = datetime.date.today()
    if isinstance(target_date, datetime.date):
        delta = target_date - today
    else:
        delta = target_date.date() - today
    if delta.days < 0:
        text = f" <span class=\"badge red white-text\">Past Due</span>"
        return mark_safe(text)
    elif delta.days == 1:
        text = f" <span class=\"badge orange white-text\">Due Tomorrow</span>"
        return mark_safe(text)
    elif delta.days == 0:
        text = f" <span class=\"badge orange white-text\">Due Today</span>"
        return mark_safe(text)
    elif delta.days <= 7:
        text = f" <span class=\"badge yellow black-text\">Due Soon</span>"
        return mark_safe(text)
    else:
        text = ''
        return mark_safe(text)


@register.filter(name='daysuntil', expects_localtime=True)
def days_until(target_date):
    today = datetime.date.today()
    if isinstance(target_date, datetime.date):
        delta = target_date - today
    else:
        delta = target_date.date() - today
    if delta.days > 1:
        text = f"<small>Due in</small><br><h5> {delta.days} days</h5>"
        return mark_safe(text)
    elif delta.days == 1:
        text = f"<small>Due</small><br><h5> Tomorrow</h5>"
        return mark_safe(text)
    elif delta.days == 0:
        text = f"<small>Due</small><br><h5> Today</h5>"
        return mark_safe(text)
    elif delta.days == -1:
        text = f"<small>Past Due</small><br><h5>{abs(delta.days)} Day</h5>"
        return mark_safe(text)
    else:
        text = f"<small>Past Due</small><br><h5>{abs(delta.days)} Days</h5>"
        return mark_safe(text)

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

