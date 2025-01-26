from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'acc'

urlpatterns = [
    path('', views.index, name=('index')),
    path('registro/', views.ViewRegistroUsuario.as_view(), name='registro'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', views.ViewPerfilUsuario.as_view(), name='perfil' ),
    path('logout/', views.custom_logout, name='logout'),
]

if settings.DEBUG: # hacemos esta validación para que servir los estaticos desde django solo en desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)