# Generated by Django 2.1.7 on 2019-03-12 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprazamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('aplicação', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
