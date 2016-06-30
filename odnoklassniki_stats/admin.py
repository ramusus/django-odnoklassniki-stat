from django.contrib import admin
from models import People

class PeopleAdmin(admin.ModelAdmin):
    fields = ('d_name', 'd_value', 'd_percentage')

admin.site.register(People, PeopleAdmin)
