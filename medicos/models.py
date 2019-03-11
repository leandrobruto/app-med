from django.db import models

# Create your models here.


class Medico(models.Model):
    nome = models.CharField(max_length=150)
    crm = models.CharField(max_length=15)

