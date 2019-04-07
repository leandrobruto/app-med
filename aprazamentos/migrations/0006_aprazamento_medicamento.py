# Generated by Django 2.1.7 on 2019-03-20 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0002_remove_medicamento_aprazamento'),
        ('aprazamentos', '0005_auto_20190312_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='aprazamento',
            name='medicamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='medicamentos.Medicamento'),
            preserve_default=False,
        ),
    ]