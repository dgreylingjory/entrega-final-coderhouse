from django import forms
from .models import * 

class ValeCombustibleForm(forms.Form):
    id = forms.IntegerField(
        required=False, 
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control w-25'})
        )
    fecha = (forms.DateField(
        label='Fecha', 
        widget=forms.DateInput(attrs={'type': 'date'})) ##permite entrada de fecha por seleccion de un calendario
        ) 
    litros_cargados = forms.IntegerField(
        label='Litros cargados', 
        max_value=999999, ##entrada numerica limitado a cantidades racionales
        min_value=1) 
    matricula_aeronave = forms.ModelChoiceField(
        queryset=Aeronave.objects.all(), ##permite seleccionar de clases aeronave
        label='Matrícula Aeronave', 
        empty_label="Seleccione una aeronave",)
    patente_camion = forms.ModelChoiceField(
        queryset=Camion.objects.all(), ##permite seleccionar de clases camion
        label='Patente camión',
        empty_label="Seleccione un camión",)
    motivo =forms.CharField(
        label='Motivo', 
        max_length=100)
    #despachador = forms.ModelChoiceField(
    #    queryset=User.objects.all(), ##permite seleccionar de clases despachador
    #    label='Despachador', 
    #    empty_label="Seleccione un despachador",)
    receptor = forms.ModelChoiceField(
        queryset=User.objects.all(), ##permite seleccionar de clases receptor
        label='Receptor', 
        empty_label="Seleccione un receptor",
        )
    def __init__(self, *args, **kwargs):
        # Automatically set the emisor field based on the logged-in user
        self.user = kwargs.pop('user', None)  # Pass user when initializing form
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['despachador'] = forms.ModelChoiceField(queryset=User.objects.filter(id=self.user.id), initial=self.user, disabled=True)

    despachador = forms.ModelChoiceField(queryset=User.objects.none(), disabled=True) 