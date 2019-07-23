from django.shortcuts import render
from .models import Aprazamento
from django.views.generic import ListView
from django.views.generic.edit import CreateView

# Create your views here.
class listaAprazamentos(ListView):
    template_name = 'aprazamento/aprazamentos.html'
    model = Aprazamento
    context_object_name = 'aprazamentos'


class addAprazamento(CreateView):
    model = Aprazamento
    template_name = 'aprazamento/add.html'
    fields = ['medicamento', 'erro', 'data_programada', 'hora_programada', 'data_aplicacao', 'hora_aplicacao', 'status']
    success_url = '/prescricoes'