# Generated by Django 2.1.7 on 2019-04-01 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aprazamentos', '0010_auto_20190401_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprazamento',
            name='medicamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aprazamentos', to='medicamentos.Medicamento'),
        ),
    ]