# Generated by Django 4.1.2 on 2023-03-13 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0012_studentprofile_sem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='Sem',
            field=models.CharField(choices=[('Sem1', 'Sem1'), ('Sem2', 'Sem2'), ('Sem3', 'Sem3'), ('Sem4', 'Sem4'), ('Sem5', 'Sem5'), ('Sem6', 'Sem6')], default='', max_length=100),
        ),
    ]
