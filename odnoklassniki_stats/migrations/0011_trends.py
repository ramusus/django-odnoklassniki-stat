# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_groups', '__first__'),
        ('odnoklassniki_stats', '0010_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trends',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('trend', models.CharField(max_length=100, choices=[(b'reach', b'reach'), (b'new_members', b'new_members'), (b'left_members', b'left_members'), (b'members_diff', b'members_diff'), (b'likes', b'likes')])),
                ('time', models.DateTimeField(null=True, blank=True)),
                ('value', models.IntegerField(null=True, blank=True)),
                ('group', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
