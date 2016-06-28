from django.db import models
from odnoklassniki_api.models import OdnoklassnikiModel, OdnoklassnikiPKModel
from odnoklassniki_groups.models import Group

#GetStatOverview
class groupGetStatOverview(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
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

#groupGetStatPeople
class People_demography_male(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
    d_name = models.CharField(max_length=50, null=True, blank=True)
    d_value = models.IntegerField(null=True, blank=True)
    d_percentage = models.FloatField(null=True, blank=True)

class People_cities(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
    c_name = models.CharField(max_length=50, null=True, blank=True)
    c_value = models.IntegerField(null=True, blank=True)
    c_percentage = models.FloatField(null=True, blank=True)

class People_references(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
    r_name = models.CharField(max_length=50, null=True, blank=True)
    r_value = models.IntegerField(null=True, blank=True)
    r_percentage = models.FloatField(null=True, blank=True)

#getStatTopic
class Topic(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
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
class getStatTopics(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
    reach = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    comments = models.IntegerField(null=True, blank=True)

#getStatTrends
class Trends_reach(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
    t_time = models.DateTimeField(null=True, blank=True)
    t_value = models.IntegerField(null=True, blank=True)

class Trends_new_members(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
    nm_time = models.DateTimeField(null=True, blank=True)
    nm_value = models.IntegerField(null=True, blank=True)

class Trends_left_members(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
    lm_time = models.DateTimeField(null=True, blank=True)
    lm_value = models.IntegerField(null=True, blank=True)

class Trends_members_diff(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
    md_time = models.DateTimeField(null=True, blank=True)
    md_value = models.IntegerField(null=True, blank=True)

class Trends_likes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gid = models.ForeignKey(Group)
    l_time = models.DateTimeField(null=True, blank=True)
    l_value = models.IntegerField(null=True, blank=True)