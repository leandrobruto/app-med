from accounts.models import User
from django.db import models

# Create your models here.


class Medico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    crm = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.usuario
