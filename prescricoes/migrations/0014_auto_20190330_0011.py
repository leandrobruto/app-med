# Generated by Django 2.1.7 on 2019-03-30 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0003_medicamento_aprazamento'),
        ('prescricoes', '0013_prescricao_medicamentos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescricao',
            name='medicamentos',
        ),
        migrations.AddField(
            model_name='prescricao',
            name='medicamentos',
            field=models.ManyToManyField(to='medicamentos.Medicamento'),
        ),
    ]
