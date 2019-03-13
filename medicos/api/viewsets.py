from rest_framework.viewsets import ModelViewSet
from medicos.models import Medico
from .serializers import MedicoSerializer


class MedicosViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
