# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0017_auto_20160629_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peoplecities',
            name='group',
        ),
        migrations.DeleteModel(
            name='PeopleCities',
        ),
        migrations.RemoveField(
            model_name='peopledemographymale',
            name='group',
        ),
        migrations.DeleteModel(
            name='PeopleDemographyMale',
        ),
        migrations.RemoveField(
            model_name='peoplereferences',
            name='group',
        ),
        migrations.DeleteModel(
            name='PeopleReferences',
        ),
        migrations.AlterField(
            model_name='people',
            name='d_name',
            field=models.CharField(max_length=50, choices=[(b'demography_male', [(b'<12', b'<12'), (b'12 - 17', b'12 - 17'), (b'18 - 24', b'18 - 24'), (b'25 - 34', b'25 - 34'), (b'35 - 44', b'35 - 44'), (b'45 - 54', b'45 - 54'), (b'55 - 64', b'55 - 64'), (b'65+', b'65+')]), (b'demography_female', [(b'<12', b'<12'), (b'12 - 17', b'12 - 17'), (b'18 - 24', b'18 - 24'), (b'25 - 34', b'25 - 34'), (b'35 - 44', b'35 - 44'), (b'45 - 54', b'45 - 54'), (b'55 - 64', b'55 - 64'), (b'65+', b'65+')]), (b'cities', b'cities'), (b'references', [(b'FEED', b'FEED'), (b'SEARCH', b'SEARCH'), (b'RECOMMENDATION', b'RECOMMENDATION'), (b'WIDGET', b'WIDGET'), (b'TARGET', b'TARGET'), (b'EXTERNAL', b'EXTERNAL'), (b'CATALOG', b'CATALOG'), (b'INVITE', b'INVITE'), (b'DISCUSSIONS', b'DISCUSSIONS'), (b'MY_GROUPS', b'MY_GROUPS')])]),
            preserve_default=True,
        ),
    ]
