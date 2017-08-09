# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlueOcean', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='pricenew',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='post',
            name='priceold',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=20),
        ),
    ]