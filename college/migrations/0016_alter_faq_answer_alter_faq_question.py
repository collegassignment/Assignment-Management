# Generated by Django 4.1.2 on 2023-03-15 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0015_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(),
        ),
    ]
