# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_stats', '0003_getstattopics_people_cities_people_demography_male_people_references_topic_trends_left_members_trend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupgetstatoverview',
            name='id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
