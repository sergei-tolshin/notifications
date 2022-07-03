from abc import ABC, abstractmethod


class AbstractService(ABC):

    @abstractmethod
    def send(self):
        pass


class BaseService(AbstractService):
    def __init__(self, event, data):
        self.event = event
        self.data = data
