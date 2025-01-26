from django.urls import reverse_lazy
from django.views.generic import DetailView,CreateView
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserEditForm, UserRegisterForm, ProfileEditForm
from django.utils.decorators import method_decorator
from .models import Profile


# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

class UserRegisterView(CreateView): ##creacion de usuario
    model = User  
    form_class = UserRegisterForm  
    template_name = 'accounts/registro.html'  
    success_url = reverse_lazy('acc:login')  

    def form_valid(self, form):
        response = super().form_valid(form)

        if not hasattr(self.object, 'profile'): ##si no hay perfil, lo crea
            Profile.objects.create(user=self.object)

        messages.success(self.request, 'Usuario creado exitosamente. ¡Ahora puedes iniciar sesión!')
        return response

@method_decorator(login_required, name='dispatch')
class ViewPerfilUsuario(DetailView): ##vista de perfil
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'usuario'
    
    def get_object(self, queryset=None):
        return self.request.user

def custom_logout(request): #cierre de sesion
    logout(request)
    return redirect('acc:login')  

@login_required
def editarPerfil(request): ##edicion de perfil
    usuario = request.user
    try:
        perfil = usuario.profile
    except Profile.DoesNotExist:
        perfil = Profile.objects.create(user=usuario)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=usuario)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('acc:index')
    else:
        user_form = UserEditForm(instance=usuario)
        profile_form = ProfileEditForm(instance=perfil)

    return render(request, "accounts/editarPerfil.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "usuario": usuario
    })


