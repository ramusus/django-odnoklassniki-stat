# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupgetstatoverview',
            name='fields',
        ),
        migrations.RemoveField(
            model_name='groupgetstatoverview',
            name='period',
        ),
        migrations.RemoveField(
            model_name='groupgetstatoverview',
            name='start_time',
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='end_time_ms',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='engagement',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='engagement_prev',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='engagement_rate',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='engagement_rate_prev',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='feedback',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='feedback_prev',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='months_ms',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='reach',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='reach_prev',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupgetstatoverview',
            name='start_time_ms',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
