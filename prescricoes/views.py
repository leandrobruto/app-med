import ast
import urllib.request
import json
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .models import Prescricao
from medicamentos.models import Medicamento
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

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['medicamento']

def detalhes(request, pk):
    submitted = False
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            prescricao = get_object_or_404(Prescricao, pk=pk)
            obj = form.save(commit=False)
            obj.prescricao = prescricao
            obj.save()
    else:
        form = MedicamentoForm()   

    req = urllib.request.Request('http://localhost:8000/api/prescricoes/' + str(pk) + "/")
    req.add_header('Content-Type', 'application/json')

    with urllib.request.urlopen(req) as response:
        r = response.read()

    prescricao = json.loads(r.decode("utf-8"))
    context = {
        'prescricao': prescricao,
        'form': form,
    }

    return render(request, 'prescricao/detalhes.html', context)

class editarPrescricao(UpdateView):
    model = Prescricao
    template_name = 'prescricao/editar.html'
    fields = ['paciente', 'leito', 'foto']
    success_url = '/prescricoes'

def deletarMedicamento(request, p, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    medicamento.delete()
    
    return redirect('detalhes_prescricao', p)
