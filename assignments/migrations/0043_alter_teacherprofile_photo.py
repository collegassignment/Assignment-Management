# Generated by Django 4.1.2 on 2023-04-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0042_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='Photo',
            field=models.ImageField(upload_to='teacherprofile/'),
        ),
    ]