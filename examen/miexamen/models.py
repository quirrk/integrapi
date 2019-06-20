from django.db import models
import datetime

class Examen(models.Model):
    cod_examen = models.AutoField(primary_key=True)
    rut_entidad = models.CharField(max_length=20)
    rut_paciente = models.CharField(max_length=20)
    fecha_solicitud = models.DateField(auto_now_add=True, null=True)
    fecha_entrega = models.DateField(blank=False, null=True)
    estado = models.CharField(max_length=200)
    rut_especialista = models.CharField(max_length=20)

    def __str__(self):
        return self.cod_examen

class ListaExamen(models.Model):
    cod_examen = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre