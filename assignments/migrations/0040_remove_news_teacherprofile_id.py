# Generated by Django 4.1.2 on 2023-04-06 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0039_alter_news_teacherprofile_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='Teacherprofile_id',
        ),
    ]
