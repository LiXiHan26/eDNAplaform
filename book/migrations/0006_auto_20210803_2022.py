# Generated by Django 2.2.10 on 2021-08-03 18:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20210803_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowrecord',
            name='borrower_card',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='end_day',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 18, 22, 7, 962041, tzinfo=utc)),
        ),
    ]
