from rest_framework.viewsets import ModelViewSet
from pacientes.models import Paciente
from .serializers import PacienteSerializer


class PacientesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

