from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts import views

app_name = 'acc'

urlpatterns = [
    path('', views.index, name=('index')),
    path('registro/', views.ViewRegistroUsuario.as_view(), name=('registro')),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', views.ViewPerfilUsuario.as_view(), name='perfil' ),
    path('logout/', LogoutView.as_view(), name='logout'),
]
