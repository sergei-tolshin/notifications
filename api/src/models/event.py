from enum import Enum
from typing import Dict, List

from pydantic import Field

from models.base import OrjsonMixin

example_payload = {
    'user_id': 'fd794c08-3d99-4646-9f7a-b4c70e9827ff',
    'email': 'user@fake.ru'
}


class AppEnum(str, Enum):
    auth: str = 'auth'
    movies: str = 'movies'
    promo: str = 'promo'
    ugc: str = 'ugc'


class NoticeMethodEnum(str, Enum):
    email: str = 'email'
    sms: str = 'sms'
    telegram: str = 'telegram'
    websocket: str = 'websocket'


class Event(OrjsonMixin):
    app: AppEnum
    type: str
    notice_method: List[NoticeMethodEnum]
    payload: Dict = Field(..., example=example_payload)
