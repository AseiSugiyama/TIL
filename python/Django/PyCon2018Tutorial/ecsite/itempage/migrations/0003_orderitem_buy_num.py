# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-16 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itempage', '0002_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='buy_num',
            field=models.PositiveIntegerField(default=1, verbose_name='数量'),
            preserve_default=False,
        ),
    ]
