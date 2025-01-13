from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import FormCreacionUsuario

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

class ViewRegistroUsuario(FormView):
    template_name = 'accounts/registro.html'  # Template for rendering the form
    form_class = FormCreacionUsuario  # The form class to use
    success_url = reverse_lazy('login')  # Redirect URL after successful registration

    def form_valid(self, form):
        # This method is called when the form is valid
        # Save the new user and perform additional actions if necessary
        form.save()  # Save the new user created by the form
        return super().form_valid(form)

