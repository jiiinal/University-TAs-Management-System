# Generated by Django 3.0.5 on 2022-06-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0015_stipendrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinator',
            name='coid',
        ),
        migrations.AddField(
            model_name='coordinator',
            name='mail',
            field=models.EmailField(default=None, max_length=30, unique=True),
        ),
    ]
