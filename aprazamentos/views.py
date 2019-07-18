from django.shortcuts import render
from .models import Aprazamento
from django.views.generic import ListView

# Create your views here.
class listaAprazamentos(ListView):
    template_name = 'aprazamento/aprazamentos.html'
    model = Aprazamento
    context_object_name = 'aprazamentos'