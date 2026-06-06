from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('payment/<int:book_id>/', views.manual_payment, name='manual_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
]