from celery import shared_task

from .base import BaseTask


@shared_task(bind=True, name='movies.new', base=BaseTask)
def new(self, **kwargs):
    # Уведомление о новом фильме или сериале
    pass
