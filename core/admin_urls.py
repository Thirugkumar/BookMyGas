from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard_alias'),
    path('bookings/', views.admin_bookings, name='admin_bookings'),
    path('inventory/', views.admin_inventory, name='admin_inventory'),
    path('customers/', views.admin_customers, name='admin_customers'),
    path('payments/', views.admin_payments, name='admin_payments'),
    path('reports/', views.admin_reports, name='admin_reports'),
    path('login/', auth_views.LoginView.as_view(template_name='core/admin_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
