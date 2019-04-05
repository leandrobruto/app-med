from django.db import models
from accounts.models import User

# Create your models here.


class Prescricao(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='prescricoes', null=True, blank=True)

    def __str__(self):
        return self.paciente.nome
