from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Vale, ModeloHelicoptero, Aeronave, Camion 
from forms import ValeCombustibleForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'fuel/index.html')

##mixin para ver si usuario es staff
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

##===================================Vale Combustible (CRUD)==============================
class ValeCreateView(LoginRequiredMixin, CreateView):
    model = Vale
    fields = ['fecha', 'litros_cargados','matricula_aeronave', 'patente_camion', 'motivo', 'despachador', 'receptor']
    form_class = ValeCombustibleForm
    template_name='fuel/vale_form.html'
    success_url = reverse_lazy('fuel/vale_list')

class ValeListView(LoginRequiredMixin, ListView):
    model = Vale
    template_name = 'fuel/vale_list.html'
    context_object_name = 'vales'

class ValeDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Vale
    template_name = 'fuel/vale_delete.html'
    success_url = reverse_lazy('fuel/vale_list')

class ValeUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Vale
    fields = ['fecha', 'litros_cargados','matricula_aeronave', 'patente_camion', 'motivo', 'despachador', 'receptor']
    form_class = ValeCombustibleForm
    template_name='fuel/vale_form.html'
    success_url = reverse_lazy('fuel/vale_list')

class ValeDetailView(DetailView):
    model = Vale
    template_name = 'fuel/vale_detail.html'

##======================================Creación de modelos==================================
##ModeloHelicoptero
class ModeloHelicopteroCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = ModeloHelicoptero
    fields = ['nombre_modelo', 'capacidad_modelo']
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel/modelo_list')

class ModeloHelicopteroListView(LoginRequiredMixin, ListView):
    model = ModeloHelicoptero
    template_name = 'fuel/modelo_list.html'
    context_object_name = 'modelos'

class ModeloHelicopteroDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = ModeloHelicoptero
    template_name = 'fuel/delete.html'
    success_url = reverse_lazy('fuel/modelo_list')

class ModeloHelicopteroDetailView(DetailView):
    model = ModeloHelicoptero
    template_name = 'detail.html'

class ModeloHelicopteroUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = ModeloHelicoptero
    fields = ['nombre_modelo', 'capacidad_modelo']
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel/modelo_list')

##Aeronave
class AeronaveCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Aeronave
    fields = ['modelo', 'capacidad', 'matricula']
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel/aeronave_list')

class AeronaveListView(LoginRequiredMixin, ListView):
    model = Aeronave
    template_name = 'fuel/aeronave_list.html'
    context_object_name = 'aeronaves'

class AeronaveDetailView(DetailView):
    model = Aeronave
    template_name = 'detail.html'

class AeronaveDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Aeronave
    template_name = 'fuel/delete.html'
    success_url = reverse_lazy('fuel/aeronave_list')

class AeronaveUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Aeronave
    fields = ['modelo', 'capacidad', 'matricula']
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel/aeronave_list')

##Camion
class CamionCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Camion
    fields = ['patente', 'capacidad', 'contenido', 'vencimiento_filtro', 'vencimiento_certificacion']
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel/aeronave_list')

class CamionListView(LoginRequiredMixin, ListView):
    model = Camion
    template_name = 'fuel/camion_list.html'
    context_object_name = 'camiones'

class CamionDetailView(DetailView):
    model = Camion
    template_name = 'detail.html'

class CamionDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Camion
    template_name = 'fuel/delete.html'
    success_url = reverse_lazy('fuel/camion_list')

class CamionUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Camion
    fields = ['patente', 'capacidad', 'contenido', 'vencimiento_filtro', 'vencimiento_certificacion']
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel/camion_list')

