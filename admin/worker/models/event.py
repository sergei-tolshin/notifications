from enum import Enum
from typing import Dict, List

from pydantic import Field

from .base import OrjsonMixin

example_payload = {
    'user_id': 'fd794c08-3d99-4646-9f7a-b4c70e9827ff',
    'email': 'user@fake.ru'
}


class NoticeMethodEnum(str, Enum):
    email: str = 'email'
    sms: str = 'sms'
    telegram: str = 'telegram'
    websocket: str = 'websocket'


class Event(OrjsonMixin):
    notice_method: List[NoticeMethodEnum]
    payload: Dict = Field(..., example=example_payload)
