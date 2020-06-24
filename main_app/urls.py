from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('bills/', views.BillList.as_view(), name='bills'),
    path('bills/paid/', views.paid_list, name='paid_list'),
    path('bills/<int:pk>/paid/', views.mark_paid, name='mark_paid'),
    path('bills/<int:pk>', views.BillDetail.as_view(), name='bill_detail'),
    path('bills/create/', views.BillCreate.as_view(), name='bills_create'),
    path('bills/<int:pk>/update/', views.BillUpdate.as_view(), name='bills_update'),
    path('bills/<int:pk>/delete/', views.BillDelete.as_view(), name='bills_delete'),
    path('dashboard/update', views.budget_update, name='budget_update'),
    path('categories/', views.categoryList, name='categories'),
]