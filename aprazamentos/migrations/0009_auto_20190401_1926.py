# Generated by Django 2.1.7 on 2019-04-01 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aprazamentos', '0008_aprazamento_medicamento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aprazamento',
            options={'ordering': ['medicamento']},
        ),
    ]
