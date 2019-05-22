from rest_framework.serializers import ModelSerializer
from prescricoes.models import Prescricao
from medicamentos.api.serializers import MedicamentoSerializer
from pacientes.api.serializers import PacienteSerializer
from accounts.api.serializers import AccountSerializer
from aprazamentos.api.serializers import AprazamentoSerializer
from aprazamentos.models import Aprazamento
from medicamentos.models import Medicamento
from accounts.models import User


class PrescricaoSerializer(ModelSerializer):
    # paciente = AccountSerializer(read_only=True)
    medicamentos = MedicamentoSerializer(many=True, read_only=True)
    aprazamentos = AprazamentoSerializer(many=True, read_only=True)

    class Meta:
        model = Prescricao
        fields = (
            'id', 'paciente', 'leito', 'medicamentos', 'aprazamentos', 'created', 'foto')
        read_only_fields = ('id',)

    # def cria_medicamentos(self, medicamentos, prescricao):
    #     for medicamento in medicamentos:
    #         med = Medicamento.objects.create(**medicamento)
    #         prescricao.medicamentos.add(med)
    #
    # def create(self, validated_data):
    #     medicamentos_data = validated_data.pop('medicamentos')
    #     aprazamentos_data = validated_data.pop('aprazamentos')
    #     prescricao = Prescricao.objects.create(**validated_data)
    #     for medicamento_data in medicamentos_data:
    #         medicamento = Medicamento.objects.create(prescricao=prescricao, **medicamento_data)
    #         for aprazamento_data in aprazamentos_data:
    #             Aprazamento.objects.create(medicamento=medicamento, **aprazamento_data)
    #     return prescricao
