# Generated by Django 2.2.10 on 2021-08-12 13:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_auto_20210812_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrecord',
            name='end_day',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 13, 56, 7, 491659, tzinfo=utc)),
        ),
    ]
