import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery(
    __name__,
    include=[
        'worker.tasks.auth',
        'worker.tasks.movies',
        'worker.tasks.promo',
        'worker.tasks.ugc'
    ]
)

app.config_from_object('worker.core.config')
