# Generated by Django 2.1.7 on 2019-02-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescricoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescricao',
            name='horario',
            field=models.CharField(max_length=10),
        ),
    ]
