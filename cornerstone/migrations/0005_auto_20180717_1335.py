# Generated by Django 2.0.6 on 2018-07-17 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0004_auto_20180710_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]