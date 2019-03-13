from django.db import models
from aprazamentos.models import Aprazamento

# Create your models here.


class Medicamento(models.Model):
    descricao = models.CharField(max_length=150)
    aprazamento = models.ForeignKey(Aprazamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
