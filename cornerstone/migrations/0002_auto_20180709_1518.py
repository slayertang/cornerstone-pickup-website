# Generated by Django 2.0.6 on 2018-07-09 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_time',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trip',
            name='unpicked_kids',
            field=models.ManyToManyField(blank=True, related_name='_trip_unpicked_kids_+', to='cornerstone.Child'),
        ),
    ]