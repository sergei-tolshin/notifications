import grpc
from celery import shared_task
from grpc_client.messages.users_pb2 import GetUsersRequest
from grpc_client.messages.users_pb2_grpc import UsersStub
from jinja2 import Template as Tpl
from notices.models import Template
from worker.models.event import Event

from .base import BaseTask


@shared_task(bind=True, name='promo.newsletter', base=BaseTask)
def newsletter(self, **kwargs):
    # Рассылка от менеджера
    event = Event(**kwargs)
    payload = event.payload
    subject = payload.get('subject')
    template_id = payload.get('template_id')

    recipients = payload.get('recipients')
    channel = grpc.insecure_channel('grpc:50051')
    client = UsersStub(channel)
    request = GetUsersRequest(**recipients)
    response = client.GetUsers(request)

    template = Template.objects.get(id=template_id)
    tpl = self.env.get_template('content.html')

    for user in response.users:
        content = Tpl(template.body).render(name=user.name)
        body = tpl.render(content=content)
        service = self.services.get('email')
        service.send(subject, body, user.email)
