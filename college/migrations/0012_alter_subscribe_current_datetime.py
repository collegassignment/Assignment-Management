# Generated by Django 4.1.2 on 2023-03-13 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0011_alter_subscribe_current_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='current_datetime',
            field=models.DateField(default=datetime.date(2023, 3, 13)),
        ),
    ]
