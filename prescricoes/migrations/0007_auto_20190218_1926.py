# Generated by Django 2.1.7 on 2019-02-18 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescricoes', '0006_auto_20190218_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescricao',
            name='medicamento',
            field=models.TextField(max_length=100),
        ),
    ]
