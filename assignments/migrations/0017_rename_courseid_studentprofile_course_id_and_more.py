# Generated by Django 4.1.2 on 2023-03-14 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0016_alter_studentprofile_sem_alter_subject_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='Courseid',
            new_name='Course_id',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='Courseid',
            new_name='Course_id',
        ),
        migrations.RenameField(
            model_name='teacherprofile',
            old_name='Courseid',
            new_name='Course_id',
        ),
    ]