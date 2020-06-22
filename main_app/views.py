from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserInfoForm
from .models import User, Bill, UserInfo
from django.db.models import Sum, Count
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class BillList(ListView):
    model = Bill
    template_name = 'main_app/bills.html'

class BillCreate(CreateView):
    model = Bill
    fields = ['name', 'description', 'amount', 'dueDate', 'category']
    success_url = '/bills/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BillUpdate(UpdateView):
    model = Bill
    fields = ['name', 'description', 'amount', 'dueDate', 'category']
    success_url = '/bills/'

class BillDelete(DeleteView):
    model = Bill
    success_url = '/bills/'

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    bills = Bill.objects.filter(user=request.user)
    context = {
        'bills': bills,
        'categories': bills.annotate(category_amount=Sum('amount')),
        'total_bills': bills.aggregate(Sum('amount')),
    }
    return render(request, 'dashboard.html', context)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        info_form = UserInfoForm(request.POST) 
        if form.is_valid() and info_form.is_valid():
            user = form.save()
            info = info_form.save(commit=False)
            info.user = user
            info.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    info_form = UserInfoForm()
    context = {
        'form': form,
        'info_form': info_form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)