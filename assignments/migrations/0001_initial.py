# Generated by Django 4.1.2 on 2023-03-09 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college', '0004_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.course')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
