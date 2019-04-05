from django.db import models
from prescricoes.models import Prescricao


# Create your models here.


class Medicamento(models.Model):
    prescricao = models.ForeignKey(Prescricao, related_name="medicamentos", on_delete=models.CASCADE)
    medicamento = models.CharField(max_length=150)
    anotacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.medicamento
