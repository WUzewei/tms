# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-14 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmsApp', '0002_auto_20160110_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('selected', models.BooleanField(default=False, editable=False, verbose_name='To Transfer?')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='upload time')),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='OsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('genre', models.CharField(choices=[('TAR', 'Tar Package'), ('RPM', 'Rpm Package'), ('DEB', 'Deb Package'), ('ISO', 'ISO Package'), ('IMG', 'IMG Package')], default='ISO', max_length=20, verbose_name='type')),
                ('selected', models.BooleanField(default=False, editable=False, verbose_name='To Install?')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='upload time')),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.AlterField(
            model_name='software',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
