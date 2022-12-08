# from __future__ import absolute_import, unicode_literals

# import os

# from celery import Celery
# from django.conf import settings

# # SETTINGS
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','app.settings.base') #always remember to change celery settings to what ever settings you are using currently
# app = Celery('app')

# app.config_from_object(settings,namespace='CELERY')
# # CELERY BEAT Settings
# app.conf.beat_schedule = {
# }

# app.autodiscover_tasks()

#************************************************************************************************

# from __future__ import absolute_import

# import os
# import sys

# import django
# from celery import Celery

# app = Celery('app')

# app.config_from_object('django.conf:settings', namespace='CELERY')

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings.base')
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
# django.setup()

# from django.conf import settings

# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


#************************************************************************************************


import os

from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery(
    'app',
    backend='redis://redis:6379/0', 
    broker='redis://redis:6379/0',
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')