from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserInfoForm
from .models import User

def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        info_form = UserInfoForm(request.POST) #This is to add the budget info into the User Creation form   
        if form.is_valid() and info_form.is_valid():
            user = form.save()
            info = info_form.save(commit=False) #Stores the budget value, commit=false will keep it in an 'unsaved' state so we can save to user at the same time
            info.user = user #assigns user to the UserInfo model (For the 1-to-1 relationship)
            info.save() ## Saves to UserInfo model
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    info_form = UserInfoForm()
    context = {
        'form': form,
        'info_form': info_form, #passes user info form to doc
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)