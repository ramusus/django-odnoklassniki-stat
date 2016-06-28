from django.shortcuts import render
from django.http import JsonResponse
from odnoklassniki_api.api import api_call
from odnoklassniki_groups.models import Group


# from oauth_tokens import api
import logging

def call(request):
    c = api_call('url.getInfo', url='https://ok.ru/sports.people')
    u = api_call('group.getInfo', uids=51658613915882, fields='group.name')
    new_obj = Group.objects.create(id=1, name=u[0].get('name'))
    new_obj.save()

    return JsonResponse({'c' : c, 'u' : u})
