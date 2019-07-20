from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import render
from .models import User
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'key': token.key, 'id': token.user_id})

class listaUsuarios(ListView):
    template_name = 'usuario/usuarios.html'
    model = User
    context_object_name = 'usuarios'

class addUsuario(CreateView):
    model = User
    template_name = 'usuario/add.html'
    fields = ['usuario', 'nome', 'nome_mae', 'credencial', 'roles', 'is_active', 'is_staff']
    success_url = '/usuarios'

class editarUsuario(UpdateView):
    model = User
    template_name = 'usuario/editar.html'
    fields = ['usuario', 'nome', 'nome_mae', 'credencial', 'roles', 'is_active', 'is_staff']
    success_url = '/usuarios'

class deletarUsuario(DeleteView):
    model = User
    template_name = 'usuario/deletar.html'
    success_url = '/usuarios'