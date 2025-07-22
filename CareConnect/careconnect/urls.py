from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('appointments/', views.appointments, name='appointments'),
    path('active_appointments/', views.active_appointments, name='active_appointments'),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/users/', views.admin_users, name='admin_users'),
    path('admin/appointments/', views.admin_appointments, name='admin_appointments'),
    path('admin/doctors/', views.admin_doctors, name='admin_doctors'),
    path('admin/doctors/add/', views.add_doctor, name='add_doctor'),
    path('admin/doctors/delete/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
    path('admin/appointments/confirm/<int:appointment_id>/', views.confirm_appointment, name='confirm_appointment'),
    path('admin/appointments/cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
]