from django import template
from django.utils.safestring import mark_safe
import random

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
    if arg:
        balance = value - arg
        if balance == 0:
            return f"You're exactly on budget. What a coincidence!"
        elif balance < 0:
            return f"You're ${abs(balance)} over your monthly budget. Time to tighten up the belt."
        else:
            return f"You're ${balance} under your budget. Go ahead and treat yo' self!"
    
@register.simple_tag(name='protip')
def random_protip():
    protips = [
        'Don’t spend more money than you have.',
        'Stick to your grocery lists – compile them based on an itemized overview of your household needs and never stray too far from it.',
        'Develop a distaste for Starbucks.',
        'Use cash. Take money out of your account and use real cash from a real wallet to pay for your daily expenses. When you run out of bills, you run out of money to spend.',
        'Exercise in the great outdoors, or use your own body weight – forget expensive gym memberships and personal trainers.',
        'Don’t keep credit cards in your wallet, or near any of your computers with an Internet connection.',
        'Preventing an impulse purchase with this motivation hack: simply think about how many hours it took you to earn that amount.',
        'There’s No One Size-Fits-All Budget. Find a Plan That Works for You',
        'Use a Budgeting App (like PGGY!) or the Envelope System to Track Your Spending on the Go',
        'Use the Past to Predict Your Future Income and Expenses',
        'Don’t Confuse Infrequent Expenses With Emergencies',
        'Remember the Obvious: You Need to Spend Less',
        'Negotiate Your Bills to Save Money',
    ]
    return random.choice(protips)