# Generated by Django 3.0.2 on 2020-02-28 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0014_auto_20200227_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
