# Generated by Django 3.0.2 on 2020-02-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0024_auto_20200229_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date_time',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
