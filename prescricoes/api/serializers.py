from rest_framework.serializers import ModelSerializer
from prescricoes.models import Prescricao


class PrescricaoSerializer(ModelSerializer):
    class Meta:
        model = Prescricao
        fields = (
            'id', 'prescricao', 'anotacoes', 'data', 'paciente', 'foto')
