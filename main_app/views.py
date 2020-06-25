from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserInfoForm
from .models import User, Bill, UserInfo, CATEGORIES
from django.db.models import Sum, Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
import datetime

class BillList(LoginRequiredMixin, ListView):
    model = Bill
    template_name = 'main_app/bills.html'
    def get_queryset(self):
        order_req = self.request.GET.get('ordering')
        if order_req:
            return Bill.objects.filter(user=self.request.user, paid=False).order_by(order_req)
        else:
            return Bill.objects.filter(user=self.request.user, paid=False).order_by('dueDate')

class BillDetail(LoginRequiredMixin, DetailView):
    model = Bill
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['same_category'] = Bill.objects.filter(category=self.object.category).exclude(pk=self.object.id)
        return context

class BillCreate(LoginRequiredMixin, CreateView):
    model = Bill
    fields = ['name', 'description', 'amount', 'dueDate', 'category']
    success_url = '/bills/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BillUpdate(LoginRequiredMixin, UpdateView):
    model = Bill
    fields = ['name', 'description', 'amount', 'dueDate', 'category']
    success_url = '/bills/'

class BillDelete(LoginRequiredMixin, DeleteView):
    model = Bill
    success_url = '/bills/'

def home(request):
    return render(request, 'home.html')

@login_required
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

@login_required
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
        'category_colors' : CATEGORIES,
    }
    return render(request, 'dashboard.html', context)

@login_required
def mark_paid(request, pk):
    bill = Bill.objects.get(id=pk)
    bill.paid = True
    bill.save()
    return redirect('/bills/')

@login_required
def paid_list(request):
    paid_bills = Bill.objects.filter(user=request.user, paid=True)
    return render(request, 'main_app/paid.html', { 'paid_bills' : paid_bills })

@login_required
def budget_update(request):
    user_info = UserInfo.objects.get(user=request.user)
    form = UserInfoForm(request.POST, instance=user_info)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
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