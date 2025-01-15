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
    template_name = 'accounts/registro.html'  # Template for rendering the form
    form_class = FormCreacionUsuario  # The form class to use
    success_url = reverse_lazy('acc:login')  # Redirect URL after successful registration

    def form_valid(self, form):
        # This method is called when the form is valid
        # Save the new user and perform additional actions if necessary
        form.save()  # Save the new user created by the form
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ViewPerfilUsuario(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'usuario'
    
    def get_object(self, queryset=None):
        return self.request.user  # Retrieve the logged-in user