from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Vale, ModeloHelicoptero, Aeronave, Camion 
from .forms import ValeCombustibleForm, CamionForm
from django.urls import reverse_lazy, reverse

# Create your views here.

##===================================Vistas de la aplicación==================================
def index(request):
    return render(request, 'fuel/index.html')

def classes(request):
    return render(request, 'fuel/seleccionar_list.html')

def classes_create(request):
    return render(request, 'fuel/seleccionar_create.html')

##mixin para ver si usuario es staff
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

##===================================Vale Combustible (CRUD)==============================
class ValeCreateView(CreateView):
    model = Vale
    form_class = ValeCombustibleForm
    template_name = 'fuel/vale_form.html'
    success_url = reverse_lazy('fuel:vale_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  
        return kwargs

    def form_valid(self, form):
        form.instance.despachador = self.request.user  ##Coloca al usuario logeado como despachador
        return super().form_valid(form)

class ValeListView(LoginRequiredMixin, ListView):
    model = Vale
    template_name = 'fuel/vale_list.html'
    context_object_name = 'vales'

class ValeDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Vale
    template_name = 'fuel/vale_delete.html'
    success_url = reverse_lazy('fuel:vale_list')

class ValeUpdateView(StaffRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Vale
    fields = ['fecha', 'litros_cargados','matricula_aeronave', 'patente_camion', 'motivo', 'despachador', 'receptor']
    template_name='fuel/vale_form.html'
    success_url = reverse_lazy('fuel:vale_list')

class ValeDetailView(DetailView):
    model = Vale
    template_name = 'fuel/vale_detail.html'
    context_object_name = 'object'
    
##======================================Creación de modelos==================================
##ModeloHelicoptero
class ModeloHelicopteroCreateView(StaffRequiredMixin, LoginRequiredMixin, CreateView):
    model = ModeloHelicoptero
    fields = ['nombre_modelo', 'capacidad_modelo']
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel:modelo_list')

class ModeloHelicopteroListView(LoginRequiredMixin, ListView):
    model = ModeloHelicoptero
    template_name = 'fuel/modelo_list.html'
    context_object_name = 'modelos'

class ModeloHelicopteroDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    model = ModeloHelicoptero
    template_name = 'fuel/modelo_delete.html'
    success_url = reverse_lazy('fuel:modelo_list')

class ModeloHelicopteroDetailView(DetailView):
    model = ModeloHelicoptero
    template_name = 'fuel/modelo_detail.html'

class ModeloHelicopteroUpdateView(StaffRequiredMixin, LoginRequiredMixin, UpdateView):
    model = ModeloHelicoptero
    fields = ['nombre_modelo', 'capacidad_modelo']
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel:modelo_list')

##Aeronave
class AeronaveCreateView(StaffRequiredMixin, LoginRequiredMixin, CreateView):
    model = Aeronave
    fields = ['modelo', 'capacidad', 'matricula']
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel:aeronave_list')

class AeronaveListView(LoginRequiredMixin, ListView):
    model = Aeronave
    template_name = 'fuel/aeronave_list.html'
    context_object_name = 'aeronaves'

class AeronaveDetailView(DetailView):
    model = Aeronave
    template_name = 'fuel/aeronave_detail.html'

class AeronaveDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Aeronave
    template_name = 'fuel/aeronave_delete.html'
    success_url = reverse_lazy('fuel:aeronave_list')

class AeronaveUpdateView(StaffRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Aeronave
    fields = ['modelo', 'capacidad', 'matricula']
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel:aeronave_list')

##Camion
class CamionCreateView(StaffRequiredMixin, LoginRequiredMixin, CreateView):
    model = Camion
    form_class = CamionForm
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel:camion_list')

class CamionListView(LoginRequiredMixin, ListView):
    model = Camion
    template_name = 'fuel/camion_list.html'
    context_object_name = 'camiones'

class CamionDetailView(DetailView):
    model = Camion
    template_name = 'fuel/camion_detail.html'

class CamionDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Camion
    template_name = 'fuel/camion_delete.html'
    success_url = reverse_lazy('fuel:camion_list')

class CamionUpdateView(StaffRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Camion
    form_class = CamionForm
    template_name='fuel/form.html'
    success_url = reverse_lazy('fuel:camion_list')

