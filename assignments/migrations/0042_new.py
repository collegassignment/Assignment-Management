# Generated by Django 4.1.2 on 2023-04-06 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0041_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Teacherprofile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.teacherprofile')),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
