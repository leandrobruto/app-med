# Generated by Django 2.1.7 on 2019-03-20 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicos', '0002_medico_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='nome',
        ),
        migrations.AddField(
            model_name='medico',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
