# Generated by Django 2.0.6 on 2018-08-26 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0008_auto_20180826_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bus',
            options={'verbose_name': 'Buses', 'verbose_name_plural': 'Buses'},
        ),
        migrations.AlterModelOptions(
            name='child',
            options={'verbose_name': 'Children', 'verbose_name_plural': 'Children'},
        ),
    ]
