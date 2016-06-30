# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnoklassniki_groups', '__first__'),
        ('odnoklassniki_stats', '0006_auto_20160628_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupStatOverview',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('reach', models.BigIntegerField(null=True, blank=True)),
                ('engagement', models.BigIntegerField(null=True, blank=True)),
                ('feedback', models.BigIntegerField(null=True, blank=True)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('reach_prev', models.BigIntegerField(null=True, blank=True)),
                ('engagement_prev', models.BigIntegerField(null=True, blank=True)),
                ('feedback_prev', models.BigIntegerField(null=True, blank=True)),
                ('engagement_rate', models.FloatField(null=True, blank=True)),
                ('engagement_rate_prev', models.FloatField(null=True, blank=True)),
                ('months', models.CharField(max_length=1000, null=True, blank=True)),
                ('gid', models.ForeignKey(to='odnoklassniki_groups.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PeopleCities',
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
            name='PeopleDemographyMale',
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
            name='PeopleReferences',
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
            name='StatTopics',
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
            name='TrendsLeftMembers',
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
            name='TrendsLikes',
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
            name='TrendsMembersDiff',
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
            name='TrendsNewMembers',
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
            name='TrendsReach',
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
        migrations.RemoveField(
            model_name='getstattopics',
            name='gid',
        ),
        migrations.DeleteModel(
            name='getStatTopics',
        ),
        migrations.RemoveField(
            model_name='groupgetstatoverview',
            name='gid',
        ),
        migrations.DeleteModel(
            name='groupGetStatOverview',
        ),
        migrations.RemoveField(
            model_name='people_cities',
            name='gid',
        ),
        migrations.DeleteModel(
            name='People_cities',
        ),
        migrations.RemoveField(
            model_name='people_demography_male',
            name='gid',
        ),
        migrations.DeleteModel(
            name='People_demography_male',
        ),
        migrations.RemoveField(
            model_name='people_references',
            name='gid',
        ),
        migrations.DeleteModel(
            name='People_references',
        ),
        migrations.RemoveField(
            model_name='trends_left_members',
            name='gid',
        ),
        migrations.DeleteModel(
            name='Trends_left_members',
        ),
        migrations.RemoveField(
            model_name='trends_likes',
            name='gid',
        ),
        migrations.DeleteModel(
            name='Trends_likes',
        ),
        migrations.RemoveField(
            model_name='trends_members_diff',
            name='gid',
        ),
        migrations.DeleteModel(
            name='Trends_members_diff',
        ),
        migrations.RemoveField(
            model_name='trends_new_members',
            name='gid',
        ),
        migrations.DeleteModel(
            name='Trends_new_members',
        ),
        migrations.RemoveField(
            model_name='trends_reach',
            name='gid',
        ),
        migrations.DeleteModel(
            name='Trends_reach',
        ),
    ]
