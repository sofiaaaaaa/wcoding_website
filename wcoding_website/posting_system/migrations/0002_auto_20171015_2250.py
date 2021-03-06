# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug_ko',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('main_window', 'Main_window'), ('meet_the_team', 'Meet_the_team'), ('regular_class', 'Regular_class'), ('classes', 'Classes'), ('camp', 'Camp'), ('best_picks', 'Best_picks'), ('news_events', 'News_events')], default='classes', max_length=20, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='thumbnail/%Y/%m/%d', verbose_name='Image'),
        ),
    ]
