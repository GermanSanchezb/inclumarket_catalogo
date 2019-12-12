from django.shortcuts import render, redirect
from .forms import ProductosForm
from .models import Productos
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class home(TemplateView):
    template_name = 'index.html'

class ListaProd(ListView):
    model = Productos
    template_name = 'lista.html'
    context_object_name = 'productos'

class CrearProd(CreateView):
    model = Productos
    template_name = 'crear_prod.html'
    form_class = ProductosForm
    success_url = reverse_lazy ('catalogo:lista')
class ModProd(UpdateView):
    model = Productos
    template_name ='mod_prod.html'
    form_class = ProductosForm
    success_url = reverse_lazy ('catalogo:lista')
class EliminarProd(DeleteView):
    model = Productos
    template_name = 'eliminar_prod.html'
    success_url = reverse_lazy('catalogo:lista')