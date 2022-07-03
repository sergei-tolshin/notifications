import asyncio

import websockets
from notices.models import DeliveryMethod

from .base import BaseService


class WebsocketService(BaseService):
    method = DeliveryMethod.WEBSOCKET
