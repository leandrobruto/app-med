# Generated by Django 2.1.7 on 2019-03-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190328_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'dsaasd'), (2, 'asdasd'), (3, 'dasdasd'), (4, 'dsasdas'), (5, 'dsadasd')], primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('is_medico', 'Médico'), ('is_enfermagem', 'Enfermagem'), ('is_farmacia', 'Farmácia'), ('is_paciente', 'Paciente'), ('is_admin', 'Admin')], default='is_medico', max_length=15),
        ),
    ]
