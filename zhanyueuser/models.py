# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class zuser(models.Model):
	zhanyue_loginName = models.CharField(max_length=40,unique=True)#登录名
	zhanyue_passwoord = models.CharField(max_length=80)#登录web系统密码
	zhanyue_useremail = models.EmailField(unique=True)
	zhanyue_userphone = models.CharField(max_length=20,blank=True, null=True)#电话
	zhanyue_jobId = models.CharField(max_length=20)#工号
	zhanyue_jobname = models.CharField(max_length=20,blank=True, null=True)#职称
	zhanyue_md5sum = models.CharField(max_length=32)

	def __unicode__(self):
		return self.zhanyue_loginName

class zgroup(models.Model):
	zhanyue_group_name = models.CharField(max_length=40,unique=True)
	zhanyue_leader = models.ForeignKey(zuser,related_name="zhanyue_leader")#组长
	zhanyue_user = models.ManyToManyField(zuser, related_name="zhanyue_user")
	def __unicode__(self):
		return self.zhanyue_group_name

class zdpmt(models.Model):
	zhanyue_dpt_name = models.CharField(max_length=40,unique=True)
	zhanyue_main_leader = models.ForeignKey(zuser,related_name="zhanyue_main_leader")#部长
	zhanyue_dpy_leader = models.ManyToManyField(zuser, related_name="zhanyue_dpy_leader")
	zhanyue_groupinfo = models.ManyToManyField(zgroup, related_name="zhanyue_groupinfo")
	def __unicode__(self):
		return self.zhanyue_dpt_name

class zblacklist(models.Model):
	zhanyue_userId = models.ForeignKey(zuser,related_name="zhanyue_userId")
	zhanyue_ip = models.IPAddressField()
	zhanyue_intime = models.DateTimeField(auto_now_add=True)
	zhanyue_outtime = models.DateTimeField(auto_now_add=True)
	zhanyue_status = models.BooleanField(default=True)
	zhanyue_commt = models.CharField(max_length=150,blank=True, null=True)

	def __unicode__(self):
		return self.zhanyue_commt