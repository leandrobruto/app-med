from django.db import models
from medicamentos.models import Medicamento

# Create your models here.


class Aprazamento(models.Model):
    medicamento = models.ForeignKey(Medicamento, related_name='aprazamentos', on_delete=models.CASCADE)
    horario = models.DateTimeField()
    aplicacao = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
            return str(self.horario)
