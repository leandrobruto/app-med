from rest_framework.serializers import ModelSerializer
from medicos.models import Medico


class MedicoSerializer(ModelSerializer):
    class Meta:
        model = Medico
        fields = (
            'id', 'nome', 'crm')
