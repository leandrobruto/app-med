# Generated by Django 2.1.7 on 2019-03-12 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aprazamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprazamento',
            name='aplicação',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aprazamento',
            name='horario',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
