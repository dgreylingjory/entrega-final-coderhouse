from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import FormCreacionUsuario, AvatarForm
from django.utils.decorators import method_decorator
from .models import Profile

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

class ViewRegistroUsuario(FormView):
    model = User
    template_name = 'accounts/registro.html'
    form_class = FormCreacionUsuario
    success_url = reverse_lazy('acc:login')

    def form_valid(self, form):
        # Save the user form to create the User instance
        user = form.save()

        # Log the user in after successful registration
        login(self.request, user)
        
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ViewPerfilUsuario(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'usuario'
    
    def get_object(self, queryset=None):
        return self.request.user

def custom_logout(request):
    logout(request)
    return redirect('acc:login')  # Or 'index' or wherever you want to redirect

@login_required
def upload_avatar(request):
    # Ensure the user has a profile
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('acc:perfil')  # Redirect back to the profile page after uploading
    else:
        form = AvatarForm(instance=request.user.profile)

    return render(request, 'accounts/upload_avatar.html', {'form': form})
