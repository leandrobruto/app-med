from rest_framework.serializers import ModelSerializer
from pacientes.models import Paciente


class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
            'id', 'nome', 'leito', 'prontuario')
