# Generated by Django 4.1.2 on 2023-04-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0027_remove_news_teacherprofile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='Teacherprofile_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assignments.teacherprofile'),
        ),
    ]