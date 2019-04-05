# Generated by Django 2.1.7 on 2019-04-01 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0003_medicamento_aprazamento'),
        ('prescricoes', '0014_auto_20190330_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescricao',
            name='medicamentos',
        ),
        migrations.AddField(
            model_name='prescricao',
            name='medicamentos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='medicamentos.Medicamento'),
            preserve_default=False,
        ),
    ]
