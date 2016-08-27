# -*- coding: utf-8 -*-
from zhanyueuser.models import *

class zhanyueUser:
	"登录"
	def login(self,name,pwd):
		zdata = zuser.objects.filter(zhanyue_loginName=name,zhanyue_passwoord=pwd)
		if zdata:
			for i in zdata[0].zhanyue_userId.filter():
				if i.zhanyue_status:
					return {"ret":False,"info":"黑名单账号,说明:%s" %(i.zhanyue_commt)}
			else:
				return {"ret":True}
		else:
			return {"ret":False,"info":"账号或者密码错误,无法登陆"}