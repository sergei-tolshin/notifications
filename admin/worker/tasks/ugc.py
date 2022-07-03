from celery import shared_task

from .base import BaseTask


@shared_task(bind=True, name='ugc.like', base=BaseTask)
def like_review(self, **kwargs):
    # Пользователь лайкнул рецензию к фильму
    pass


@shared_task(bind=True, name='ugc.reminder', base=BaseTask)
def reminder_favorites(self, **kwargs):
    # Напоминание про список отложенных фильмов,
    # когда он долгое время неизменялся
    pass


@shared_task(bind=True, name='ugc.top10', base=BaseTask)
def top10(self, **kwargs):
    # ТОП-10 фильмов недели
    pass
