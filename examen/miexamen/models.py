from django.db import models
from datetime import datetime, timedelta

class ListaExamen(models.Model):
    cod_examen = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Examen(models.Model):
    cod_examen = models.AutoField(primary_key=True)
    tipo_examen = models.ForeignKey(ListaExamen, on_delete=models.CASCADE, null=True)
    rut_entidad = models.CharField(max_length=20, default='60536429-8')
    rut_paciente = models.CharField(max_length=20)
    fecha_solicitud = models.DateField(auto_now_add=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=200, default='En curso')
    rut_especialista = models.CharField(max_length=20, default='13548987-8')

    def __str__(self):
        return self.cod_examen