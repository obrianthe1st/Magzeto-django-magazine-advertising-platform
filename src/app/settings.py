"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#We are now setting the authenticated user model to the one in which we created
AUTH_USER_MODEL = 'authors.Author'



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #local
    'core',
    'apps.authors',
    'apps.article',
    'apps.category',
    'apps.ads.dashboard',
    'apps.ads.campaign',
    'apps.ads.advert',
    'apps.ads.billing',
    'apps.ads.analytics',

    #third party
    'celery',
    'django_celery_results',
    'django_celery_beat',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.category.context_processors.menu_links',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'PORT': os.environ.get('PORT'),
    }
}

#celery url
broker_url = "redis://redis:6379/0"

#redis_url= "redis://redis:6379/0"
result_backend = 'redis://redis:6379/0'

#CACHE_BACKEND = "redis_cache"


#CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
accept_content = ['application/json']
result_serializer = 'json'
task_serializer = 'json'

timezone ='America/NewYork'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),
                    os.path.join(BASE_DIR, 'media')]

#this will be for the cdn
STATIC_ROOT = os.path.join(BASE_DIR,'static_cdn') 
MEDIA_ROOT = os.path.join(BASE_DIR,'media_cdn') 


STATICFILES_FINDERS = [
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

####################################################################################################

if DEBUG:
     MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')



if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1


#all-auth configuration'
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "none"

LOGIN_REDIRECT_URL = '/'

ACCOUNT_FORMS = {
'signup': 'apps.authors.forms.CustomSignupForm',
}

ACCOUNT_LOGOUT_REDIRECT_URL ='/'
ACCOUNT_LOGIN_REDIRECT_URL ='/'

ACCOUNT_SIGNUP_REDIRECT_URL = "/"

#######################################################################################################

# LOGGING = {
#     'version':1,
#     'disable_existing_loggers': False,

#     'formatters': {
#         "verbose":{
#             "format":"{asctime} - {levelname} - {lineno} - {module} - {message}",
#             "style": "{",
#         },

#     },

#     'handlers': {
#         'console': { # this handler logs to the console
#             'class': "logging.StreamHandler", #streamhandler writes the logging to the console
#             'formatter': "verbose",
#         },

#         'log_file':{
#             'class': "logging.FileHandler",
#             'filename': f"{BASE_DIR}/logs/info.log",
#             "formatter": "verbose",

#         },

#         'log_db':{
#             'class': "logging.FileHandler",
#             'filename': f"{BASE_DIR}/logs/db.log",
#             "formatter": "verbose",
#         },

#     },

#     'loggers': {
#         'main': {
#             'handlers': ['log_file','console'],
#             'propogate': True,
#             'level': 'INFO',
#         },
#         'main2': {
#             'handlers': ['log_db','console'],
#             'propogate': True,
#             'level': 'WARNING',
#         },

#     },
# }



