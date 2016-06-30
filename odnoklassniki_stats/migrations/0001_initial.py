# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_groups', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='groupGetStatOverview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', models.CharField(blank=True, max_length=1000, null=True, choices=[(b'DAY', b'DAY'), (b'WEEK', b'WEEK'), (b'MOUNTH', b'MOUNTH')])),
                ('start_time', models.BigIntegerField()),
                ('fields', models.CharField(max_length=1000)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
