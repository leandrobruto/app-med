# Generated by Django 2.1.7 on 2019-02-18 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento', models.CharField(max_length=150)),
                ('dosagem', models.CharField(max_length=20)),
                ('via', models.CharField(max_length=10)),
                ('horario', models.TimeField()),
                ('anotacoes', models.TextField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente')),
            ],
        ),
    ]
