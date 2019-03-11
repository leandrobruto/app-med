from rest_framework.viewsets import ModelViewSet
from prescricoes.models import Prescricao
from .serializers import PrescricaoSerializer


class PrescricoesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer
