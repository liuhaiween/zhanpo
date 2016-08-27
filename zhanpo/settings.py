# -*- coding: utf-8 -*-
"""
Django settings for zhanpo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nso(c9dt=u_8g%nu5+rz^ayqh0c2hwqs6k*lz$4dlu(m_fda&w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'zhanyueuser',
	'zhanyueBase',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	# 'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zhanpo.urls'

WSGI_APPLICATION = 'zhanpo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
"测试为本地地址"
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': "zhanpo",
		'USER': "root",
		'PASSWORD': "liuhaiwen+5688",
		'HOST': "localhost",
		'PORT': "3306",
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
os.path.join(BASE_DIR, "static"),
)

##email
EMAIL_HOST='pop3.liuhaiwen.com'
EMAIL_PORT= 25
EMAIL_HOST_USER = 'zhanpo@liuhaiwen.com'
EMAIL_HOST_PASSWORD = '2YXSeZBysAlI3q'
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

"10分钟不操作,重启登录(秒)"
timeout=6