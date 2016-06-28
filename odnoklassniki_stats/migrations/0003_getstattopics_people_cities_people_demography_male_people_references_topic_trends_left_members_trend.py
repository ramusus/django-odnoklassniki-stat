# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_groups', '__first__'),
        ('odnoklassniki_stats', '0002_auto_20160627_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='getStatTopics',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('reach', models.IntegerField(null=True, blank=True)),
                ('likes', models.IntegerField(null=True, blank=True)),
                ('comments', models.IntegerField(null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='People_cities',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('c_name', models.CharField(max_length=50, null=True, blank=True)),
                ('c_value', models.IntegerField(null=True, blank=True)),
                ('c_percentage', models.FloatField(null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='People_demography_male',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('d_name', models.CharField(max_length=50, null=True, blank=True)),
                ('d_value', models.IntegerField(null=True, blank=True)),
                ('d_percentage', models.FloatField(null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='People_references',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('r_name', models.CharField(max_length=50, null=True, blank=True)),
                ('r_value', models.IntegerField(null=True, blank=True)),
                ('r_percentage', models.FloatField(null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('tid', models.BigIntegerField()),
                ('renderings', models.BigIntegerField(null=True, blank=True)),
                ('reach', models.BigIntegerField(null=True, blank=True)),
                ('engagement', models.BigIntegerField(null=True, blank=True)),
                ('feedback', models.BigIntegerField(null=True, blank=True)),
                ('reach_own', models.BigIntegerField(null=True, blank=True)),
                ('reach_earned', models.BigIntegerField(null=True, blank=True)),
                ('renderings_own', models.BigIntegerField(null=True, blank=True)),
                ('renderings_earned', models.BigIntegerField(null=True, blank=True)),
                ('content_opens', models.BigIntegerField(null=True, blank=True)),
                ('feedback_total', models.BigIntegerField(null=True, blank=True)),
                ('likes', models.BigIntegerField(null=True, blank=True)),
                ('comments', models.BigIntegerField(null=True, blank=True)),
                ('reshares', models.IntegerField(null=True, blank=True)),
                ('video_plays', models.IntegerField(null=True, blank=True)),
                ('music_plays', models.IntegerField(null=True, blank=True)),
                ('link_clicks', models.IntegerField(null=True, blank=True)),
                ('negatives', models.BigIntegerField(null=True, blank=True)),
                ('hides_from_feed', models.BigIntegerField(null=True, blank=True)),
                ('complaints', models.IntegerField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trends_left_members',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('lm_time', models.DateTimeField(null=True, blank=True)),
                ('lm_value', models.IntegerField(null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trends_likes',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('l_time', models.DateTimeField(null=True, blank=True)),
                ('l_value', models.IntegerField(null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trends_members_diff',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('md_time', models.DateTimeField(null=True, blank=True)),
                ('md_value', models.IntegerField(null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trends_new_members',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('nm_time', models.DateTimeField(null=True, blank=True)),
                ('nm_value', models.IntegerField(null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trends_reach',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('t_time', models.DateTimeField(null=True, blank=True)),
                ('t_value', models.IntegerField(null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
