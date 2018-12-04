from django.db import models

class Producto( models.Model ):
    id_prod = models.AutoField( primary_key = True )
    nombre_prod = models.CharField( max_length = 120, blank = False , null = False )
    costo_pre = models.IntegerField( default= 0 )
    costo_real = models.IntegerField( default= 0 )
    nota = models.CharField( max_length = 200 )

    def __str__( self ):
        return self.nombre_prod

class Usuario( models.Model ):
    id_user = models.AutoField( primary_key = True )
    nombre_user = models.CharField( max_length = 120, blank = False , null = False )
    correo = models.CharField( max_length = 35, blank = False , null = False )
    contraseña = models.CharField( max_length = 50, blank = False, null = False )

class Listado( models.Model ):
    id_lista = models.AutoField( primary_key = True )
    nombre_list = models.CharField( max_length = 80, blank = False, null = False )
    usuario = models.ForeignKey( Usuario, blank = False, null = False, on_delete = models.CASCADE )
    producto = models.ForeignKey( Producto, blank = False, null = False, on_delete = models.CASCADE )

    def __str__( self ):
        return self.nombre_list

class Tienda( models.Model ):
    id_tienda = models.AutoField( primary_key = True )
    nombre_tienda = models.CharField( max_length = 80, blank = False , null = False )
    nombre_sucur = models.CharField( max_length = 120, blank = False , null = False )
    direccion = models.CharField( max_length = 200, blank = False , null = False )
    ciudad = models.CharField( max_length = 50, blank = False , null = False )
    region = models.CharField( max_length = 50, blank = False , null = False )