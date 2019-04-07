# Generated by Django 2.1.7 on 2019-03-29 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190328_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('is_medico', 'Médico'), ('is_enfermagem', 'Enfermagem'), ('is_farmacia', 'Farmácia'), ('is_paciente', 'Paciente'), ('is_admin', 'Admin')], default='is_medico', max_length=15, verbose_name='Tipo'),
        ),
    ]