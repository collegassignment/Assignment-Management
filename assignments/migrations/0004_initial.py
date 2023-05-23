# Generated by Django 4.1.2 on 2023-03-09 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college', '0007_course'),
        ('assignments', '0003_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacherprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='')),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Contact', models.IntegerField()),
                ('Email', models.CharField(max_length=100)),
                ('Address', models.TextField(default='')),
                ('Dateofjoin', models.DateField(default='')),
                ('Courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.course')),
            ],
            options={
                'db_table': 'teacherprofile',
            },
        ),
    ]
