# Generated by Django 3.0.2 on 2020-02-28 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0016_comment_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date_time',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]