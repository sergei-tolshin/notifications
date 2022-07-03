from notices.models import DeliveryMethod

from .base import BaseService


class SMSService(BaseService):
    method = DeliveryMethod.SMS
