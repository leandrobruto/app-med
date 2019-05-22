from rest_framework.serializers import ModelSerializer
from accounts.api.serializers import AccountSerializer
from aprazamentos.api.serializers import AprazamentoSerializer
from medicamentos.models import Medicamento
from aprazamentos.models import Aprazamento


class MedicamentoSerializer(ModelSerializer):
    paciente = AccountSerializer(read_only=True)
    aprazamentos = AprazamentoSerializer(many=True)

    class Meta:
        model = Medicamento
        fields = (
            'id', 'prescricao', 'paciente', 'medicamento', 'aprazamentos', 'anotacoes')
        read_only_fields = ('id',)

    def create(self, validated_data):
        print(validated_data)
        aprazamentos_data = validated_data.pop('aprazamentos')
        medicamento = Medicamento.objects.create(**validated_data)
        for aprazamento_data in aprazamentos_data:
            Aprazamento.objects.create(medicamento=medicamento, **aprazamento_data)
        return medicamento