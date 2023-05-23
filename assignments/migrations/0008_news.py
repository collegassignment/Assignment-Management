# Generated by Django 4.1.2 on 2023-03-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0007_studentprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
