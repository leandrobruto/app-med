"""med_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import CustomObtainAuthToken
from accounts.api.viewsets import AccountsViewSet
from medicos.api.viewsets import MedicosViewSet
from pacientes.api.viewsets import PacientesViewSet
from medicamentos.api.viewsets import MedicamentosViewSet
from aprazamentos.api.viewsets import AprazamentosViewSet
from prescricoes.api.viewsets import PrescricoesViewSet
from teste.api.viewsets import TesteViewSet

router = routers.DefaultRouter()
router.register(r'usuario', AccountsViewSet)
router.register(r'prescricoes', PrescricoesViewSet)
router.register(r'medicos', MedicosViewSet)
router.register(r'pacientes', PacientesViewSet)
router.register(r'medicamentos', MedicamentosViewSet)
router.register(r'aprazamentos', AprazamentosViewSet)
router.register(r'teste', TesteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path(r'authenticate/', CustomObtainAuthToken.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
