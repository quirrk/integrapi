from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from miexamen import views

router = routers.DefaultRouter()
router.register(r'usuarios',views.UsuarioViewSet)
router.register(r'productos',views.ProductoViewSet)
router.register(r'tiendas',views.TiendaViewSet)
router.register(r'listados',views.ListadoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include( router.urls ) ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
