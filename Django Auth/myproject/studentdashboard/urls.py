from django.urls import path
from . import views

from django.contrib.auth import views as auth_views # later for the login

app_name = 'studentdashboard'

urlpatterns = [
    
    path('', views.student_dashboard, name='student_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='myproject/login.html'), name='login'),
    
]
