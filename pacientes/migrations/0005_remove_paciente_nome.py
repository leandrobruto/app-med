# Generated by Django 2.1.7 on 2019-03-20 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_paciente_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='nome',
        ),
    ]
