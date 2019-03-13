from django.db import models

# Create your models here.


class Aprazamento(models.Model):
    horario = models.DateTimeField()
    aplicacao = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.horario)
