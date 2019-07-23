from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaAprazamentos.as_view(), name='aprazamentos'),
    path('add/', views.addAprazamento.as_view(), name='add_aprazamento'),
    # path('editar/<int:pk>', views.editarAprazamento.as_view(), name='editar_aprazamento'),
    # path('deletar/<int:pk>', views.deletarAprazamento.as_view(), name='deletar_aprazamento')
]
