# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200511_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='function',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='price',
            field=models.DecimalField(blank=True, default=0, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='consignee',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=6, default='secret', choices=[('male', '男'), ('female', '女'), ('secret', '保密')]),
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=11, blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='classify',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
