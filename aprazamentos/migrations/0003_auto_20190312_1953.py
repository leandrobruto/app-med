# Generated by Django 2.1.7 on 2019-03-12 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aprazamentos', '0002_auto_20190312_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprazamento',
            name='horario',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
