from abc import ABC, abstractmethod
from typing import Optional


class AbstractProducer(ABC):

    @abstractmethod
    async def send_task(self, *args, **kwargs) -> None:
        pass


producer: Optional[AbstractProducer] = None


async def get_producer() -> AbstractProducer:
    return producer
