from rest_framework.viewsets import ModelViewSet
from aprazamentos.models import Aprazamento
from .serializers import AprazamentoSerializer


class AprazamentosViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Aprazamento.objects.all()
    serializer_class = AprazamentoSerializer
    filter_fields = ('id', 'erro',)
