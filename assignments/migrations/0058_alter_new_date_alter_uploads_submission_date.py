# Generated by Django 4.1.2 on 2023-05-10 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0057_alter_new_date_alter_uploads_submission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 5, 10)),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='Submission_Date',
            field=models.DateField(default=datetime.date(2023, 5, 10)),
        ),
    ]