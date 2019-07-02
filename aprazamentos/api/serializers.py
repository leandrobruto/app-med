from rest_framework.serializers import ModelSerializer
from aprazamentos.models import Aprazamento


class AprazamentoSerializer(ModelSerializer):

    class Meta:
        model = Aprazamento
        fields = (
            'id', 'erro', 'data_programada', 'hora_programada', 'data_aplicacao', 'hora_aplicacao', 'status')
        read_only_fields = ('id',)

