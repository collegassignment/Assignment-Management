# Generated by Django 4.1.2 on 2023-03-28 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0031_alter_studentprofile_sem'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofile',
            name='Teacher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
