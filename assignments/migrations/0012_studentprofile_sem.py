# Generated by Django 4.1.2 on 2023-03-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0011_alter_teacherprofile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='Sem',
            field=models.CharField(choices=[('sem1', 'sem1'), ('sem2', 'sem2'), ('sem3', 'sem3'), ('sem4', 'sem4'), ('sem5', 'sem5'), ('sem6', 'sem6')], default='', max_length=100),
        ),
    ]
