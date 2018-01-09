#coding: utf-8
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 读取数据库配置文件
config_file = os.path.join(BASE_DIR, '.env')
with open(config_file) as f:
    config = f.read()
    DATABASES_CONFIG = json.loads(config)
#apidoc 文件路径
APIDOC_DIR = os.path.join(BASE_DIR, 'doc/')
SECRET_KEY = 'ycf-pgl5de5(jvye84akz21eww1f@7s^f2pe0rwr-b&zlkb8#6'
DB_ENGINE = 'django.db.backends.mysql'  # 默认mysql连接
DB_WAIT_TIMEOUT = 29  # 单个连接最长维持时间
DB_POOL_SIZE = 16  # 连接池最大连接数
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'tbkt_system_dj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tbkt_system_dj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': 'ticket_system',  # Or path to database file if using sqlite3.
        'USER': DATABASES_CONFIG['USER'],
        'PASSWORD': DATABASES_CONFIG['PASSWORD'],
        'HOST': DATABASES_CONFIG['HOST'],
        'PORT': DATABASES_CONFIG['PORT'],  # Set to empty string for default. Not used with sqlite3.
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
