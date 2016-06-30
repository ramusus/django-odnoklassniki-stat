# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0012_remove_trends_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='trends',
            name='time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
