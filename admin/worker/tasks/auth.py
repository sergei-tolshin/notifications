import grpc
from celery import shared_task
from grpc_client.messages.users_pb2 import GetEmailConfirmRequest
from grpc_client.messages.users_pb2_grpc import UsersStub
from jinja2 import Template as Tpl
from notices.models import DeliveryMethod, Template
from worker.models.event import Event

from .base import BaseTask


@shared_task(bind=True, name='auth.registration', base=BaseTask)
def confirm_email(self, **kwargs):
    event = Event(**kwargs)
    payload = event.payload
    subject = 'Успешная регистрация'

    user_id = payload.get('user_id')
    channel = grpc.insecure_channel('grpc:50051')
    client = UsersStub(channel)
    request = GetEmailConfirmRequest(id=user_id)
    response = client.GetEmailConfirm(request)

    template = Template.objects.get(
        notice__event__name='registration',
        notice__method=DeliveryMethod.EMAIL,
        by_default=True
    )
    tpl = self.env.get_template('content.html')

    content = Tpl(template.body).render(name=response.name)
    body = tpl.render(content=content)
    service = self.services.get('email')
    service.send(subject, body, response.email)


@shared_task(bind=True, name='auth.confirm_tel', base=BaseTask)
def confirm_tel(self, **kwargs):
    # Подтверждение телефона
    pass


@shared_task(bind=True, name='auth.login', base=BaseTask)
def login(self, **kwargs):
    # Уведомление о входе
    pass


@shared_task(bind=True, name='auth.two_fa', base=BaseTask)
def two_fa(self, **kwargs):
    # Отправка кода двухфакторной аутентификации
    pass
