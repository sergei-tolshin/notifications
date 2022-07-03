import os

import sendgrid
from notices.models import DeliveryMethod
from sendgrid.helpers.mail import Content, Email, Mail

from .base import BaseService


class EmailService(BaseService):
    method = DeliveryMethod.EMAIL

    def send(subject: str, body: str,
             to_email: str, from_email='noreply@exampl.ru'):
        message = Mail(
            from_email=Email(from_email),
            to_email=Email(to_email),
            subject=subject,
            content=Content("text/plain", body)
        )
        sg = sendgrid.SendGridAPIClient(
            apikey=os.environ.get("SENDGRID_API_KEY"))
        response = sg.client.message.send.post(request_body=message.get())
        return response
