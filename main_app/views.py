from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserInfoForm
from .models import User, Bill, UserInfo, CATEGORIES
from django.db.models import Sum, Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
import datetime

class BillList(ListView):
    model = Bill
    template_name = 'main_app/bills.html'
    ordering = 'name'
    def get_queryset(self):
        return Bill.objects.filter(user=self.request.user)
    def get_ordering(self):
        return self.request.GET.get('ordering', 'name')
    def get_context_data(self, *args, **kwargs):
        context = super(BillList, self).get_context_data(*args, **kwargs)
        context['current_order'] = self.get_ordering()
        return context
    

class BillDetail(DetailView):
    model = Bill
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['same_category'] = Bill.objects.filter(category=self.object.category).exclude(pk=self.object.id)
        return context

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

def categoryList(request):
    bills = Bill.objects.filter(user=request.user)
    categories_total = {}
    for x in CATEGORIES:
        c = bills.filter(category=x[0])
        t = c.aggregate(Sum('amount'))
        if t['amount__sum']:
            categories_total[x[1]] = t['amount__sum']
    context = {
        'bills': bills,
        'total_bills': bills.aggregate(Sum('amount')),
        'categories_total': categories_total,
    }
    return render(request, 'main_app/categories.html', context)

def dashboard(request):
    bills = Bill.objects.filter(user=request.user)
    categories_total = {}
    for x in CATEGORIES:
        c = bills.filter(category=x[0])
        t = c.aggregate(Sum('amount'))
        if t['amount__sum']:
            categories_total[x[1]] = t['amount__sum']
    context = {
        'bills': bills,
        'total_bills': bills.aggregate(Sum('amount')),
        'categories_total': categories_total,
    }
    return render(request, 'dashboard.html', context)

def budget_update(request):
    user_info = UserInfo.objects.get(user=request.user)
    form = UserInfoForm(request.POST, instance=user_info)
    if form.is_valid():
        form.save()
    return render(request, 'budget.html', { 'form' : form })

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