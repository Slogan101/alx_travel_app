import os
from alx_travel_app.celery_app import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
