# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0005_auto_20160628_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupgetstatoverview',
            old_name='months_ms',
            new_name='months',
        ),
        migrations.RemoveField(
            model_name='groupgetstatoverview',
            name='end_time_ms',
        ),
        migrations.RemoveField(
            model_name='groupgetstatoverview',
            name='start_time_ms',
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='end_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='start_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
