from functools import lru_cache

from db.message_broker import AbstractProducer, get_producer
from fastapi import Depends

from .base import BaseService

# from .mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin


class NoticesService(BaseService):
    async def send_notice(self, name) -> None:
        return self.producer.send_task('tasks.test', kwargs={'name': name})


@lru_cache()
def get_notices_service(
        producer: AbstractProducer = Depends(get_producer),
) -> NoticesService:
    return NoticesService(producer)
