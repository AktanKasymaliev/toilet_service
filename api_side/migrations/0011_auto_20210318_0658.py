# Generated by Django 3.1.7 on 2021-03-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_side', '0010_auto_20210318_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Долгота'),
        ),
    ]
