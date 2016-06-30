# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0016_auto_20160629_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trendsleftmembers',
            name='group',
        ),
        migrations.DeleteModel(
            name='TrendsLeftMembers',
        ),
        migrations.RemoveField(
            model_name='trendsmembersdiff',
            name='group',
        ),
        migrations.DeleteModel(
            name='TrendsMembersDiff',
        ),
        migrations.RemoveField(
            model_name='trendsnewmembers',
            name='group',
        ),
        migrations.DeleteModel(
            name='TrendsNewMembers',
        ),
        migrations.RemoveField(
            model_name='trendsreach',
            name='group',
        ),
        migrations.DeleteModel(
            name='TrendsReach',
        ),
    ]
