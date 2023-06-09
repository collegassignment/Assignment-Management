# Generated by Django 4.1.2 on 2023-03-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0024_alter_teacherprofile_teacher_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='Course_id',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='Sem',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='Student_id',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='Teacher_id',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='Sem',
            field=models.CharField(choices=[('Sem1', 'Sem1'), ('Sem2', 'Sem2'), ('Sem3', 'Sem3'), ('Sem4', 'Sem4'), ('Sem5', 'Sem5')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Semester',
            field=models.CharField(choices=[('Sem1', 'Sem1'), ('Sem2', 'Sem2'), ('Sem3', 'Sem3'), ('Sem4', 'Sem4'), ('Sem5', 'Sem5')], default='', max_length=100),
        ),
    ]
