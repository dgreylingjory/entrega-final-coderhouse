from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from accounts import views

app_name = 'acc'

urlpatterns = [
    path('', views.index, name=('index')),
    path('registro/', views.ViewRegistroUsuario.as_view(), name=('registro')),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='acc.login'),
    ##"""path('profile/', )"""
]
