from django import forms
from django.contrib.auth.models import User
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['budget']
        help_texts = {
            'budget': 'Enter your monthly budget.',
        }