# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0015_auto_20160629_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trendslikes',
            name='group',
        ),
        migrations.DeleteModel(
            name='TrendsLikes',
        ),
    ]
