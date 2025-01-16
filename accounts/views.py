from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import FormCreacionUsuario
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

class ViewRegistroUsuario(FormView): ##ver si se puede cambiar a CreateView
    template_name = 'accounts/registro.html'  
    form_class = FormCreacionUsuario  
    success_url = reverse_lazy('acc:login')  

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ViewPerfilUsuario(DetailView): ##read, devuelve el user para la template de perfil 
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'usuario'
    
    def get_object(self, queryset=None):
        return self.request.user 