# Generated by Django 2.1.7 on 2019-05-06 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescricoes', '0022_auto_20190402_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescricao',
            name='leito',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]