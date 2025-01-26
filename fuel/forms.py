from django import forms
from .models import * 

##Formulario creacion de vale
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
        self.user = kwargs.pop('user', None)  ##encuentra el usuario logeado
        super().__init__(*args, **kwargs)

        ##hace que receptor sea nombre apellido en vez de nombre de usuario
        self.fields['receptor'].widget.choices = [
            (user.id, f"{user.first_name} {user.last_name}") for user in User.objects.all()
        ]
        
        ##hace que despachador sea el usuario logeado
        if self.user:
            self.fields['despachador'].widget.choices = [
                (self.user.id, f"{self.user.first_name} {self.user.last_name}") ##hace que sea nombre apellido en vez de username
            ]
            self.fields['despachador'].initial = self.user.id
            
        if not self.instance.pk: ##hace que numero de vale sea el ultimo + 1 automaticamente
            self.fields['id'].initial = Vale.objects.latest('id').id + 1 if Vale.objects.exists() else 1 

##Formulario creacion de camion (para tener seleccion de fecha)
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