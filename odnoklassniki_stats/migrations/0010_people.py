# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_groups', '__first__'),
        ('odnoklassniki_stats', '0009_auto_20160629_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('d_name', models.CharField(max_length=50, choices=[(b'demography_male', (b'name', ((b'<12', b'<12'), (b'12 - 17', b'12 - 17'), (b'18 - 24', b'18 - 24'), (b'25 - 34', b'25 - 34'), (b'35 - 44', b'35 - 44'), (b'45 - 54', b'45 - 54'), (b'55 - 64', b'55 - 64'), (b'65+', b'65+')))), (b'cities', b'cities'), (b'references', (b'name', ((b'FEED', b'FEED'), (b'SEARCH', b'SEARCH'), (b'RECOMMENDATION', b'RECOMMENDATION'), (b'WIDGET', b'WIDGET'), (b'TARGET', b'TARGET'), (b'EXTERNAL', b'EXTERNAL'), (b'CATALOG', b'CATALOG'), (b'INVITE', b'INVITE'), (b'DISCUSSIONS', b'DISCUSSIONS'), (b'MY_GROUPS', b'MY_GROUPS'))))])),
                ('d_value', models.IntegerField()),
                ('d_percentage', models.FloatField()),
                ('group', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
