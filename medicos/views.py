from django.shortcuts import render
from .models import Medico
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class listaMedicos(ListView):
    template_name = 'medico/medicos.html'
    model = Medico
    context_object_name = 'medicos'

class addMedico(CreateView):
    model = Medico
    template_name = 'medico/add.html'
    fields = ['usuario','crm','cpf']
    success_url = '/medicos'

class editarMedico(UpdateView):
    model = Medico
    template_name = 'medico/editar.html'
    fields = ['usuario','crm','cpf']
    success_url = '/medicos'

class deletarMedico(DeleteView):
    model = Medico
    template_name = 'medico/deletar.html'
    success_url = '/medicos'

