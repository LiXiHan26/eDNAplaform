# Generated by Django 2.2.10 on 2021-08-02 13:03

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_borrowrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowrecord',
            name='end_day',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 16, 13, 3, 27, 124051, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='borrowrecord',
            name='start_day',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]