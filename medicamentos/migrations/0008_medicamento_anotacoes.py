# Generated by Django 2.1.7 on 2019-04-02 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0007_auto_20190401_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='anotacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
