# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0018_auto_20160629_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='d_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='d_percentage',
            new_name='percentage',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='d_value',
            new_name='value',
        ),
    ]
