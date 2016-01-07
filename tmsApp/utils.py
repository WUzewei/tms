from __future__ import unicode_literals

from django.db import models
from fabric.api import *
from django.contrib import admin
from .commons import *
from fabfile import *
from .models import *

def getUserName(modeladmin, request, queryset):
    #host_num = len(queryset)
    output = execute(get_user_name, hosts = getHostList(queryset))
    saveResult2Db(output)
    # output is a dictionary
    # which like {u'192.168.233.138': 'dev1', u'192.168.233.139': 'dev2'}
    
   #rows_updated = queryset.update(status = 1)
   #     if rows_updated == 1:
   #         message_bit = "1 computer was"
   #     else:
   #         message_bit = "%s computers were" % rows_updated

   #    self.message_user(request,"%s successfully done." % message_bit)

getUserName.short_description = "Get User Name"

def getCPUInfo(modeladmin, request, queryset):
    output = execute(get_cpu_info, hosts = getHostList(queryset))
    saveResult2Db(output)
    '''
    for k,v in output.items():
	term = Terminal.objects.get(ip = k)
	print term
	term.cpu_vendor = v.get('cpu_vendor')
	print str(v.get('cpu_vendor'))
	term.cpu_cores = v.get('cpu_cores')
	term.cpu_speed = v.get('cpu_speed')
	term.cache_size = v.get('cache_size')
	term.save()
    '''
getCPUInfo.short_description = "Get CPU infomation"
