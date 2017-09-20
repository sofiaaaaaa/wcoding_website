# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 13:07
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('posting_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
