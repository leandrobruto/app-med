from django.shortcuts import render
from .models import Paciente
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class listaPacientes(ListView):
    template_name = 'pacientes.html'
    model = Paciente
    context_object_name = 'pacientes'

class addPaciente(CreateView):
    model = Paciente
    template_name = 'paciente_add.html'
    fields = ['nome','prontuario','leito']
    success_url = '/pacientes'

class editarPaciente(UpdateView):
    model = Paciente
    template_name = 'paciente_editar.html'
    fields = ['nome','prontuario','leito']
    success_url = '/pacientes'

class deletarPaciente(DeleteView):
    model = Paciente
    template_name = 'paciente_deletar.html'
    success_url = '/pacientes'

