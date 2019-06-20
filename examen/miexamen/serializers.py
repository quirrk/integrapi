from .models import Examen, ListaExamen
from rest_framework import serializers

class ListaExamenSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = ListaExamen
        fields = ( 'cod_examen', 'nombre')

class ExamenSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta: 
        model = Examen
        fields = ( 'cod_examen','rut_entidad','rut_paciente','fecha_solicitud', 'fecha_entrega', 'estado', 'rut_especialista')