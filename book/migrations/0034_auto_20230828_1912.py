# Generated by Django 2.2.10 on 2023-08-28 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0033_auto_20230828_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrecord',
            name='end_day',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 4, 19, 12, 22, 812162)),
        ),
    ]