from django import forms
from django.contrib.auth.models import User
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['budget']
        help_texts = {
            'budget': 'You can enter an amount up to $9,999,999.99. If that is your montly budget, let\'s be friends!',
        }