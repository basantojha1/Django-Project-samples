# Generated by Django 4.1.5 on 2023-01-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Title goes here', max_length=100),
        ),
    ]