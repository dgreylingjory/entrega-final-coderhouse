from django.contrib import admin
from .models import ModeloHelicoptero, Aeronave, Camion, Vale

# Register your models here.
admin.site.register(ModeloHelicoptero)
admin.site.register(Aeronave)
admin.site.register(Camion)
admin.site.register(Vale)