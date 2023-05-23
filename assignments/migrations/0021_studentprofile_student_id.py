# Generated by Django 4.1.2 on 2023-03-24 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0020_remove_news_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='Student_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
