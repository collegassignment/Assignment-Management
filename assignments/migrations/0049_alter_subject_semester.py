# Generated by Django 4.1.2 on 2023-04-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0048_remove_uploads_subject_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='Semester',
            field=models.CharField(default='', max_length=100),
        ),
    ]
