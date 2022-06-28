from functools import lru_cache

from db.message_broker import AbstractProducer, get_producer
from fastapi import Depends

from .base import BaseService


class NoticesService(BaseService):
    async def send_notice(self, event) -> None:
        task = '{app}.{type}'.format(app=event.app, type=event.type)
        data = {
            'notice_method': event.notice_method,
            'payload': event.payload
        }
        return self.producer.send_task(task, kwargs=data)


@lru_cache()
def get_notices_service(
        producer: AbstractProducer = Depends(get_producer),
) -> NoticesService:
    return NoticesService(producer)
