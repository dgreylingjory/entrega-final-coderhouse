from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Vale
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'fuel/index.html')

##===================================Vale Combustible==============================
class ValeCreateView(CreateView):
    model = Vale
    fields = ['fecha', 'litros_cargados','matricula_aeronave', 'patente_camion', 'motivo', 'despachador', 'receptor']
    template_name='fuel/vale_form.html'
    success_url = reverse_lazy('fuel/vale_list')

class ValeListView(ListView):
    model = Vale
    template_name = 'fuel/vale_list.html'
    context_object_name = 'vales'

class ValeDeleteView(DeleteView):
    model = Vale
    template_name = 'fuel/vale_delete.html'
    success_url = reverse_lazy('fuel/vale_list')

class ValeUpdateView(UpdateView):
    model = Vale
    fields = ['fecha', 'litros_cargados','matricula_aeronave', 'patente_camion', 'motivo', 'despachador', 'receptor']
    template_name='fuel/vale_form.html'
    success_url = reverse_lazy('fuel/vale_list')