# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0008_auto_20160629_0651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peoplecities',
            old_name='gid',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='peopledemographymale',
            old_name='gid',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='peoplereferences',
            old_name='gid',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='stattopics',
            old_name='gid',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='gid',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='trendsleftmembers',
            old_name='gid',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='trendslikes',
            old_name='gid',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='trendsmembersdiff',
            old_name='gid',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='trendsnewmembers',
            old_name='gid',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='trendsreach',
            old_name='gid',
            new_name='group',
        ),
    ]
