from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaMedicos.as_view(), name='medicos'),
    path('add/', views.addMedico.as_view(), name='add_medico'),
    path('editar/<int:pk>', views.editarMedico.as_view(), name='editar_medico'),
    path('deletar/<int:pk>', views.deletarMedico.as_view(), name='deletar_medico')
]
