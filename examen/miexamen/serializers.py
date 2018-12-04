from .models import Usuario, Producto , Tienda, Listado 
from rest_framework import serializers

class UsuarioSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta: 
        model = Usuario
        fields = ( 'id_user','nombre_user','correo','contraseña' )

class ProductoSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Producto
        fields = ( 'id_prod','nombre_prod','costo_pre','costo_real','nota' )

class TiendaSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Tienda
        fields = ( 'id_tienda','nombre_tienda','nombre_sucur','direccion','ciudad','region' )

class ListadoSerializers( serializers.HyperlinkedModelSerializer ):
    class Meta: 
        model = Listado
        fields = ('id_lista','nombre_list','usuario','producto')