from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from miexamen import views

router = routers.DefaultRouter()
router.register(r'examenes',views.ExamenViewSet)
router.register(r'listaexamenes',views.ListaExamenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include( router.urls ) ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]