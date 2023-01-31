"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""

import os
from celery import Celery
from celery.schedules import crontab


# этот код скопирован с manage.py
# он установит модуль настроек по умолчанию Django для приложения 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liceum38.settings')

# имя приложения
app = Celery("announcements")

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# загрузка tasks.py в приложение django
app.autodiscover_tasks()

# Далее идут скрипты, запускаемые в определенное время


app.conf.beat_schedule = {
    # Executes every day at  12:30 pm.
    'delete_expired_values_task': {
        'task': 'announcements.tasks.delete_expired_values',
        'schedule': crontab(hour=0, minute=0),
        'args': (),
    },
}