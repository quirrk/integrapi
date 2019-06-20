from .models import Examen, ListaExamen
from rest_framework import viewsets
from .serializers import ExamenSerializer, ListaExamenSerializer
import json

class ListaExamenViewSet( viewsets.ModelViewSet ):
    queryset = ListaExamen.objects.all()
    serializer_class = ListaExamenSerializer

class ExamenViewSet( viewsets.ModelViewSet ):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer