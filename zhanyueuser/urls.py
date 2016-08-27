# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include,url
from zhanyueuser.views import *


urlpatterns = patterns('zhanyueuser.views',
	url(r'^login$', zhanyue_login),
	)