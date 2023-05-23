# Generated by Django 4.1.2 on 2023-03-28 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('college', '0018_delete_user'),
        ('assignments', '0022_alter_studentprofile_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofile',
            name='Teacher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='Sem',
            field=models.CharField(choices=[('Sem1', 'Sem1'), ('Sem2', 'Sem2'), ('Sem3', 'Sem3'), ('Sem4', 'Sem4'), ('Sem5', 'Sem5')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='Course_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='college.course'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='Sem',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='Student_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Semester',
            field=models.CharField(choices=[('Sem1', 'Sem1'), ('Sem2', 'Sem2'), ('Sem3', 'Sem3'), ('Sem4', 'Sem4'), ('Sem5', 'Sem5')], default='', max_length=100),
        ),
    ]
