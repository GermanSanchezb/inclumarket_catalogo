from django.urls import path
from .views import ListaProd, CrearProd, ModProd, EliminarProd

urlpatterns = [
    path('lista/', ListaProd.as_view(), name = 'lista'),
    path('crear_prod/', CrearProd.as_view(), name = 'crear_prod'),
    path('mod_prod/<int:pk>', ModProd.as_view(), name = 'mod_prod'),
    path('eliminar_prod/<int:pk>', EliminarProd.as_view(), name = 'eliminar_prod')
]
