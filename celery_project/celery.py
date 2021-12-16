from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')


app = Celery('celery_project')

#changing default timezone 
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')   
    #print('Request: {0!r}'.format(self.request))