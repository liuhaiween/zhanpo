# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from zhanyueuser.views import index
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zhanpo.views.home', name='home'),
    # url(r'^zhanpo/', include('zhanpo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #"用户处理模块"
    url(r'^zuser/', include('zhanyueuser.urls')),

    #首页
    url(r'^$', index),
)
