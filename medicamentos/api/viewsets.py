from rest_framework.viewsets import ModelViewSet
from medicamentos.models import Medicamento
from .serializers import MedicamentoSerializer


class MedicamentosViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
