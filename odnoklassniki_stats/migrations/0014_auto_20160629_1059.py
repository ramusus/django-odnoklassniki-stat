# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0013_trends_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='d_name',
            field=models.CharField(max_length=50, choices=[(b'demography_male', ((b'<12', b'<12'), (b'12 - 17', b'12 - 17'), (b'18 - 24', b'18 - 24'), (b'25 - 34', b'25 - 34'), (b'35 - 44', b'35 - 44'), (b'45 - 54', b'45 - 54'), (b'55 - 64', b'55 - 64'), (b'65+', b'65+'))), (b'cities', b'cities'), (b'references', ((b'FEED', b'FEED'), (b'SEARCH', b'SEARCH'), (b'RECOMMENDATION', b'RECOMMENDATION'), (b'WIDGET', b'WIDGET'), (b'TARGET', b'TARGET'), (b'EXTERNAL', b'EXTERNAL'), (b'CATALOG', b'CATALOG'), (b'INVITE', b'INVITE'), (b'DISCUSSIONS', b'DISCUSSIONS'), (b'MY_GROUPS', b'MY_GROUPS')))]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trends',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
            preserve_default=True,
        ),
    ]
