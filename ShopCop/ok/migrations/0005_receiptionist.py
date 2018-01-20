# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-13 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ok', '0004_salesperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_username', models.CharField(max_length=50)),
                ('emp_name', models.CharField(max_length=250)),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ok.ShopManager')),
            ],
        ),
    ]