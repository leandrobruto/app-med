from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaPrescricoes.as_view(), name='prescricoes'),
    # path('add/', views.addPrescricao.as_view(), name='add_prescricao'),
    # path('editar/<int:pk>', views.editarPrescricao.as_view(), name='editar_prescricao'),
    # path('deletar/<int:pk>', views.deletarPrescricao.as_view(), name='deletar_prescricao')
]
