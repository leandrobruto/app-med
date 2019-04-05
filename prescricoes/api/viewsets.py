from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from prescricoes.models import Prescricao
from .serializers import PrescricaoSerializer


class PrescricoesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer

    @action(methods=['post'], detail=True)
    def associa_paciente(self, request, id):
        paciente = request.data['id']

        prescricao = Prescricao.objects.get(id=id)

        prescricao.paciente.set(paciente)

        prescricao.save()
        return HttpResponse('OK')
