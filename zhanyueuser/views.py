# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,redirect,render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
import json,time,os
"导入斩月用户处理事务"
from zhanyueuser.zuser_api import *
"导入装饰器"
from zhanyueBase.views import judgeuserLougin
usernames,passwords="root","xxx"

"首页处理视图"
@judgeuserLougin()
def index(request):
	if request.method == "GET":
		return render_to_response("ok.html")


def zhanyue_login(request):
	if request.method == "GET":
		return render_to_response("index.html")
	else:
		username = request.POST['username']
		password = request.POST['password']
		zu = zhanyueUser()
		getdata = zu.login(username,password)
		if getdata['ret']:
			global usernames,passwords
			request.session['user'] = json.dumps({"user":username,"date":time.time(),"password":password})
			usernames = username
			passwords = password
			return redirect(reverse('zhanyueuser.views.index', args=[]))
		else:
			info = getdata['info']
			return render_to_response("index.html",locals())

