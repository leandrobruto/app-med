from django.shortcuts import render
from .models import Prescricao
from django.views.generic import ListView

# Create your views here.
class listaPrescricoes(ListView):
    template_name = 'prescricao/prescricoes.html'
    model = Prescricao
    context_object_name = 'prescricoes'