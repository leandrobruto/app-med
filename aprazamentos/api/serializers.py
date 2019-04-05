from rest_framework.serializers import ModelSerializer
from aprazamentos.models import Aprazamento


class AprazamentoSerializer(ModelSerializer):

    class Meta:
        model = Aprazamento
        fields = (
            'horario', 'aplicacao', 'status')
