# Generated by Django 3.0.2 on 2020-02-28 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0015_comment_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
