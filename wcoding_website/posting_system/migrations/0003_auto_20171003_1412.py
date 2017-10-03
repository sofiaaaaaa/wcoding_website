# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting_system', '0002_auto_20171001_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('main_window', 'Main_window'), ('meet_the_team', 'Meet_the_team'), ('regular_class', 'Regular_class'), ('classes', 'Classes'), ('camp', 'Camp'), ('best_picks', 'Best_picks'), ('news_events', 'News_events')], default='classes', max_length=10),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
