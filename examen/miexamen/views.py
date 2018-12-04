from .models import Usuario, Producto , Tienda, Listado 
from rest_framework import viewsets
from .serializers import UsuarioSerializer, ProductoSerializer, TiendaSerializer, ListadoSerializers

class UsuarioViewSet( viewsets.ModelViewSet ):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProductoViewSet( viewsets.ModelViewSet ):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TiendaViewSet( viewsets.ModelViewSet ):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

class ListadoViewSet( viewsets.ModelViewSet ):
    queryset = Listado.objects.all()
    serializer_class = ListadoSerializers