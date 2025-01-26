from django import forms
from .models import * 

class ValeCombustibleForm(forms.ModelForm):
    class Meta:
        model = Vale
        fields = ['fecha', 'litros_cargados', 'matricula_aeronave', 'patente_camion', 'motivo', 'receptor']
    
    id = forms.IntegerField(
        required=False, 
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control w-25'})
    )
    fecha = forms.DateField(
        label='Fecha', 
        widget=forms.DateInput(attrs={'type': 'date'}) 
    )
    litros_cargados = forms.IntegerField(
        label='Litros cargados', 
        max_value=999999, 
        min_value=1
    )
    matricula_aeronave = forms.ModelChoiceField(
        queryset=Aeronave.objects.all(),
        label='Matrícula Aeronave', 
        empty_label="Seleccione una aeronave"
    )
    patente_camion = forms.ModelChoiceField(
        queryset=Camion.objects.all(),
        label='Patente camión',
        empty_label="Seleccione un camión"
    )
    motivo = forms.CharField(
        label='Motivo', 
        max_length=100
    )
    receptor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Receptor', 
        empty_label="Seleccione un receptor",
    )
    
    despachador = forms.ModelChoiceField(queryset=User.objects.none(), disabled=True)
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Pass user when initializing form
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['despachador'] = forms.ModelChoiceField(queryset=User.objects.filter(id=self.user.id), initial=self.user, disabled=True)

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['patente', 'capacidad', 'contenido', 'vencimiento_filtro', 'vencimiento_certificacion']
    
    patente = forms.CharField(
        label='Patente', 
        max_length=6
    )
    capacidad = forms.IntegerField(
        label='Capacidad', 
        max_value=999999, 
        min_value=1
    )
    contenido = forms.IntegerField(
        label='Contenido', 
        max_value=999999, 
        min_value=1
    )
    vencimiento_filtro = forms.DateField(
        label='Vencimiento Filtro', 
        widget=forms.DateInput(attrs={'type': 'date'}) 
    )
    vencimiento_certificacion = forms.DateField(
        label='Vencimiento Certificación', 
        widget=forms.DateInput(attrs={'type': 'date'}) 
    )