# Generated by Django 4.1.2 on 2023-03-09 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='contact',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='courseid',
            new_name='Courseid',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='Name',
        ),
    ]
