import ast
import urllib.request
import json
from django.shortcuts import render
from .models import Prescricao
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView

# Create your views here.
class listaPrescricoes(ListView):
    template_name = 'prescricao/prescricoes.html'
    model = Prescricao
    context_object_name = 'prescricoes'

class addPrescricao(CreateView):
    model = Prescricao
    template_name = 'prescricao/add.html'
    fields = ['paciente', 'leito', 'foto']
    success_url = '/prescricoes'

def detalhes(request, pk):
    req = urllib.request.Request('http://localhost:8000/api/prescricoes/' + str(pk) + "/")
    req.add_header('Content-Type', 'application/json')

    with urllib.request.urlopen(req) as response:
        r = response.read()

    prescricao = json.loads(r.decode("utf-8"))
    context = {
        'prescricao': prescricao
    }

    return render(request, 'prescricao/detalhes.html', context)

class editarPrescricao(UpdateView):
    model = Prescricao
    template_name = 'prescricao/editar.html'
    fields = ['paciente', 'leito', 'foto']
    success_url = '/prescricoes'