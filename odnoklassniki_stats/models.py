from django.db import models
from odnoklassniki_api.models import OdnoklassnikiModel, OdnoklassnikiPKModel
from odnoklassniki_groups.models import Group

DEMOGRAPHY_TYPE = [
    '<12',
    '12 - 17',
    '18 - 24',
    '25 - 34',
    '35 - 44',
    '45 - 54',
    '55 - 64',
    '65+',
]
REFERENCES_TYPE = [
    'FEED',
    'SEARCH',
    'RECOMMENDATION',
    'WIDGET',
    'TARGET',
    'EXTERNAL',
    'CATALOG',
    'INVITE',
    'DISCUSSIONS',
    'MY_GROUPS',
]

TRENDS_TYPE = [
    'reach',
    'new_members',
    'left_members',
    'members_diff',
    'likes',
]

PEOPLE_STAT_CHOICES = (('demography_male', [(type, type) for type in DEMOGRAPHY_TYPE]),
                       ('demography_female', [(type, type) for type in DEMOGRAPHY_TYPE]),
                       ('cities', 'cities'),
                       ('references', [(type, type) for type in REFERENCES_TYPE]),
                       )
TRENDS_CHOICES = [(type, type) for type in TRENDS_TYPE]

class Trends(models.Model):
    group = models.ForeignKey(Group)
    trend = models.CharField(max_length=100, choices=TRENDS_CHOICES)
    time = models.DateTimeField(null=True)
    value = models.IntegerField(null=True, blank=True)

class People(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=50, choices=PEOPLE_STAT_CHOICES)
    value = models.IntegerField()
    percentage = models.FloatField()

#GetStatOverview
class GroupStatOverview(models.Model):
    id = models.BigIntegerField(primary_key=True)
    group = models.ForeignKey(Group)
    reach = models.BigIntegerField(null=True, blank=True)
    engagement = models.BigIntegerField(null=True, blank=True)
    feedback = models.BigIntegerField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    reach_prev = models.BigIntegerField(null=True, blank=True)
    engagement_prev = models.BigIntegerField(null=True, blank=True)
    feedback_prev = models.BigIntegerField(null=True, blank=True)
    engagement_rate = models.FloatField(null=True, blank=True)
    engagement_rate_prev = models.FloatField(null=True, blank=True)
    months = models.CharField(max_length=1000, null=True, blank=True)

#getStatTopic
class Topic(models.Model):
    group = models.ForeignKey(Group)
    tid = models.BigIntegerField()
    renderings = models.IntegerField(null=True, blank=True)
    reach = models.IntegerField(null=True, blank=True)
    engagement = models.IntegerField(null=True, blank=True)
    feedback = models.IntegerField(null=True, blank=True)
    reach_own = models.IntegerField(null=True, blank=True)
    reach_earned = models.IntegerField(null=True, blank=True)
    renderings_own = models.IntegerField(null=True, blank=True)
    renderings_earned = models.IntegerField(null=True, blank=True)
    content_opens = models.IntegerField(null=True, blank=True)
    feedback_total = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    comments = models.IntegerField(null=True, blank=True)
    reshares = models.IntegerField(null=True, blank=True)
    video_plays = models.IntegerField(null=True, blank=True)
    music_plays = models.IntegerField(null=True, blank=True)
    link_clicks = models.IntegerField(null=True, blank=True)
    negatives = models.IntegerField(null=True, blank=True)
    hides_from_feed = models.IntegerField(null=True, blank=True)
    complaints = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

#getStatTopics
class StatTopics(models.Model):
    group = models.ForeignKey(Group)
    reach = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    comments = models.IntegerField(null=True, blank=True)
