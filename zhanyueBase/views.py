# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,redirect
import json,time,subprocess,os
from django.core.mail import send_mail

"导入时间限制,10分钟不做操作,则会退出"
from zhanpo.settings import timeout
"导入查询"
from zhanyueuser.zuser_api import *
"导入Ansible"
import ansible.runner
"导入urllib2"
import urllib2
# Create your views here.
"用户登录装饰器,可更新时间,档超过特定时间,那么就需要重新登,同时每次操作action的是时候都会触发更新上一次时间"
def judgeuserLougin(user=""):
	def _deco(func):
		def __deco(request, *args, **kwargs):
			user = request.session.get('user',default='root')
			if user == "root":
				return redirect(reverse('zhanyueuser.views.zhanyue_login', args=[]))
			else:
				juser = json.loads(user)
				print juser
				print time.time() - juser['date']
				passwordx = juser['password']
				usernamex = juser['user']
				"更新最近操作时间,防止被系统甩出去"
				request.session['user'] = json.dumps({"user":usernamex,"date":time.time(),"password":passwordx})
				
				"查询"
				jusers = zhanyueUser()
				getData = jusers.login(usernamex,passwordx)
				print getData
				if time.time() - juser['date'] > timeout:
					del request.session['user']
					info = "距离上次操作已经过去%d秒了,超过10分钟未操作,请重新登录" %( int(time.time() - juser['date']))
					return render_to_response("index.html",locals())

				if not getData['ret']:
					info = getData['info']
					return render_to_response("index.html",locals())
				return func(request, *args, **kwargs)
		return __deco
	return _deco