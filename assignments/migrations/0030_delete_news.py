# Generated by Django 4.1.2 on 2023-04-06 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0029_remove_news_teacherprofile_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='news',
        ),
    ]
