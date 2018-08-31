"""
Django settings for DjoSiteDba project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm6*_l!wu_wm-gzt7!8r42r%^2687yu4oh7klqy31do+lw9-fsq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []


# SET WOKRING ENV AND DB PASSWORD
# COULD SET MULTIPUL TARGET SERVER
SERVER_HOSTNAME_SET = 'iZbp1iil3e0qqrfbczpmkhZ' + 'PGS-20180113SZM' + '' 

LOCAL_HOSTNAME = socket.gethostname()
#ip = socket.gethostbyname(hostname)
#print ip
#print(LOCAL_HOSTNAME)
if (SERVER_HOSTNAME_SET.find(LOCAL_HOSTNAME) < 0):
    IS_FORMAL_DEPLOYMENT = False
    LOCAL_DB_PASSWORD = 'xiaohui@bxxh';
else:
    IS_FORMAL_DEPLOYMENT = True
    LOCAL_DB_PASSWORD = 'bxxhbxxh';

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#     'DappDbTest',
    'DappDbF1sym',
    'DappDbF2cm',
    'DappDbF3dm',
    'DappDbF4icm',
    'DappDbF5fm',
    'DappDbF6pm',
    'DappDbF7ads',
    'DappDbF8psm',
    'DappDbF9gism',
    'DappDbF10oam',
    'DappDbF11faam',
    'DappDbFxprcm',
    'DappDbSnr'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjoSiteDba.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'DjoSiteDba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Comments Options setting will remove running WARNING.


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         'NAME': 'djztest6',
#         'USER': 'root',
#         'PASSWORD': LOCAL_DB_PASSWORD,
#         'HOST': '127.0.0.1',
#         'PORT': 3306,
# #         'OPTIONS': {
# #             'autocommit': True,
# #             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
# #         },
#         'CONN_MAX_AGE': None,
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'Django',
        'USER': 'mfunhcu',
        'PASSWORD': 'xiaohui@bxxh',
        'HOST': '127.0.0.1',
        'PORT': 3306,
#         'OPTIONS': {
#             'autocommit': True,
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
        'CONN_MAX_AGE': None,
    }
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'


