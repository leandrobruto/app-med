# Generated by Django 2.1.7 on 2019-03-12 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aprazamentos', '0004_auto_20190312_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
                ('aprazamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aprazamentos.Aprazamento')),
            ],
        ),
    ]
