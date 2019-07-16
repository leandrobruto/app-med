from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaUsuarios.as_view(), name='usuarios'),
    path('add/', views.addUsuario.as_view(), name='add_usuario'),
    path('editar/<int:pk>', views.editarUsuario.as_view(), name='editar_usuario'),
    path('deletar/<int:pk>', views.deletarUsuario.as_view(), name='deletar_usuario')
]