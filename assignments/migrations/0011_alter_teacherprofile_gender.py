# Generated by Django 4.1.2 on 2023-03-13 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0010_alter_subject_subjectcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
    ]