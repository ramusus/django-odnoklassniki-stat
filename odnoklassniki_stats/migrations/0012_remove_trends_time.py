# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0011_trends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trends',
            name='time',
        ),
    ]
