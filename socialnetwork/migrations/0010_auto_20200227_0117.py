# Generated by Django 3.0.2 on 2020-02-27 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0009_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_profile',
        ),
    ]
