# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testvoc', '0002_choice_correct_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
