from abc import ABC, abstractmethod

from db.message_broker import AbstractProducer


class AbstractService(ABC):
    @abstractmethod
    async def send_notice(self):
        pass


class BaseService(AbstractService):
    def __init__(self, producer: AbstractProducer):
        self.producer: AbstractProducer = producer
