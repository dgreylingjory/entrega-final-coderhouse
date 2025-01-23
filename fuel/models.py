from django.db import models
from django.contrib.auth.models import User

# Create your models here.

##============================ MODELOS USADOS EN APP DE COMBUSTIBLE ==============================
class ModeloHelicoptero(models.Model):
    nombre_modelo = models.CharField(max_length = 10)
    capacidad_modelo = models.IntegerField()
    def __str__(self):
        return self.nombre_modelo
    def describir(self):
        return f"Modelo: {self.nombre_modelo}\nCapacidad: {self.capacidad_modelo}"
    
class Aeronave(models.Model):
    modelo = models.ForeignKey(
        ModeloHelicoptero,
        on_delete=models.CASCADE,
        related_name='modelo'
        )
    capacidad = models.IntegerField()
    matricula = models.CharField(max_length=6)
    def __str__(self):
        return self.matricula
    def describir(self):
        return f"Matrícula: {self.matricula}\nModelo: {self.modelo}\nCapacidad: {self.capacidad}"

class Camion(models.Model):
    patente = models.CharField(max_length=6)
    capacidad = models.IntegerField()
    contenido = models.IntegerField()
    vencimiento_filtro = models.DateField()
    vencimiento_certificacion = models.DateField()
    def __str__(self):
        return self.patente
    def describir(self):
        return f"Patente: {self.patente}\nCapacidad: {self.capacidad}\nContenido: {self.contenido}\nVencimiento Filtro: {self.vencimiento_filtro}\nVencimiento Certificación: {self.vencimiento_certificacion}"


##============================ MODELO PARA FORMULARIO DE VALE ===================================    
class Vale(models.Model): ##transforma la entrada del form a un objeto
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    litros_cargados = models.IntegerField()
    matricula_aeronave = models.ForeignKey(Aeronave, on_delete=models.CASCADE)
    patente_camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100)
    despachador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emite_vale')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recibe_vale')
    
    def __str__(self):
        return f"Vale {self.id} - {self.fecha}"
    

