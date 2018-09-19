# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-16 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itempage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('address', models.CharField(max_length=255, verbose_name='住所')),
                ('email', models.CharField(max_length=255, verbose_name='メールアドレス')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='注文日時')),
            ],
            options={
                'verbose_name': '注文',
                'verbose_name_plural': '注文',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=255, verbose_name='商品コード')),
                ('item_name', models.CharField(max_length=255, verbose_name='商品名')),
                ('price', models.PositiveIntegerField(verbose_name='価格')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itempage.Order')),
            ],
            options={
                'verbose_name': '注文商品',
                'verbose_name_plural': '注文商品',
                'db_table': 'order_item',
            },
        ),
    ]
