# Generated by Django 4.1.2 on 2023-03-10 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0008_subscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='current_datetime',
            field=models.DateField(default=datetime.datetime(2023, 3, 10, 13, 30, 45, 877957)),
        ),
    ]