from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaPacientes.as_view(), name='pacientes'),
    path('add/', views.addPaciente.as_view(), name='add_paciente'),
    path('editar/<int:pk>', views.editarPaciente.as_view(), name='editar_paciente'),
    path('deletar/<int:pk>', views.deletarPaciente.as_view(), name='deletar_paciente')
]
