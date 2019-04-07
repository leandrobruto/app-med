# Generated by Django 2.1.7 on 2019-04-01 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_paciente_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='usuario',
        ),
        migrations.AddField(
            model_name='paciente',
            name='leito',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='prontuario',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]