from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('bills/', views.BillList.as_view(), name='bills'),
    path('bills/create/', views.BillCreate.as_view(), name='bills_create'),
]