# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='cashback',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='commission',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='referral',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
