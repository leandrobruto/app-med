from rest_framework.serializers import ModelSerializer
from medicamentos.models import Medicamento


class MedicamentoSerializer(ModelSerializer):
    class Meta:
        model = Medicamento
        fields = (
            'id', 'descricao', 'aprazamento')
