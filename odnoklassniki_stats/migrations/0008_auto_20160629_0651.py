# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0007_auto_20160628_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupstatoverview',
            old_name='gid',
            new_name='group',
        ),
    ]
