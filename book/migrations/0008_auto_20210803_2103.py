# Generated by Django 2.2.10 on 2021-08-03 19:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20210803_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowrecord',
            name='borrower_email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='borrowrecord',
            name='borrower_phone_number',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='end_day',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 19, 3, 27, 55621, tzinfo=utc)),
        ),
    ]
