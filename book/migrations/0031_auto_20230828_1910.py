# Generated by Django 2.2.10 on 2023-08-28 19:10

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0030_auto_20211226_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmblDownloadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Database', models.CharField(max_length=100, verbose_name='database')),
                ('OriginalDownloadFile', models.CharField(max_length=200, verbose_name='original')),
            ],
        ),
        migrations.CreateModel(
            name='MitofishDownloadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OriginalDownloadFile', models.CharField(max_length=200, verbose_name='original')),
            ],
        ),
        migrations.CreateModel(
            name='NcbiDownloadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_Address', models.EmailField(max_length=32, verbose_name='email')),
                ('Database', models.CharField(max_length=100, verbose_name='database')),
                ('Query', models.CharField(max_length=100, verbose_name='query')),
                ('Batch_Size', models.IntegerField(verbose_name='batch_size')),
                ('OriginalDownloadFile', models.CharField(max_length=200, verbose_name='original')),
                ('SpeciesFile', models.FileField(default='fake_path', upload_to='', verbose_name='speciesfile')),
            ],
        ),
        migrations.CreateModel(
            name='Primers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Query', models.CharField(max_length=100, unique=True, verbose_name='Query')),
                ('Forword_Primer', models.CharField(max_length=100, unique=True, verbose_name='Forword_Primer')),
                ('Reverse_Primer', models.CharField(max_length=100, unique=True, verbose_name='Forword_Primer')),
                ('Sequence_Quantity', models.PositiveIntegerField(verbose_name='Sequence_quantity')),
                ('Created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created_at')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_by',
            field=models.CharField(default='2112124016', max_length=20),
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='end_day',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 4, 19, 10, 6, 588817)),
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accession', models.CharField(max_length=100, verbose_name='Accession')),
                ('Taxonomy_ID', models.CharField(max_length=100, verbose_name='Taxonomy_ID')),
                ('Kingdom', models.CharField(max_length=100, verbose_name='Kingdom')),
                ('Dividion', models.CharField(max_length=100, verbose_name='Dividion')),
                ('Class', models.CharField(max_length=100, verbose_name='Class')),
                ('Order', models.CharField(max_length=100, verbose_name='Order')),
                ('Family', models.CharField(max_length=100, verbose_name='Family')),
                ('Genus', models.CharField(max_length=100, verbose_name='Genus')),
                ('Species', models.CharField(max_length=100, verbose_name='Species')),
                ('Sequence_Description', models.CharField(max_length=5000, unique=True, verbose_name='Sequence_Description')),
                ('Loaction', models.CharField(max_length=100, verbose_name='Loaction')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created_Time')),
                ('Primers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Primers', to='book.Primers')),
            ],
        ),
    ]
