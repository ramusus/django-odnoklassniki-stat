from django.shortcuts import render, HttpResponse, render_to_response
from django.http import JsonResponse
from odnoklassniki_api.api import api_call
from odnoklassniki_groups.models import Group
from models import People, Trends
import datetime

# from oauth_tokens import api
import logging

def call(request):
    c = api_call('url.getInfo', url='https://ok.ru/sports.people')
    # u = api_call('group.getStatTopic', topic_id=65743876063466, fields='renderings')
    u = api_call('group.getStatOverview', gid=51658613915882, fields='group.name')

    # new_obj = Group.objects.create(id=1, name=u[0].get('name'))
    # new_obj.save()

    return JsonResponse({'c' : c, 'u' : u})

def getPeople(request):
    new_obj = Trends.objects.create(id=4, group=Group.objects.get(pk=1), trend='ddd', value=1748518)
    new_obj.save()
    print new_obj.get_trend_display()

    return render_to_response('dfljn')
