# Generated by Django 2.1.7 on 2019-04-01 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prescricoes', '0015_auto_20190401_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescricao',
            name='medicamentos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicamentos', to='medicamentos.Medicamento'),
        ),
    ]
