from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaPrescricoes.as_view(), name='prescricoes'),
    path('add/', views.addPrescricao.as_view(), name='add_prescricao'),
    path('detalhes/<int:pk>', views.detalhes, name='detalhes_prescricao'),
    path('detalhes/<int:p>/deletar_medicamento/<int:pk>', views.deletarMedicamento, name='deletar_medicamento'),
    path('editar/<int:pk>', views.editarPrescricao.as_view(), name='editar_prescricao'),
]
