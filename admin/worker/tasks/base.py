from celery import Task
from jinja2 import Environment, FileSystemLoader
from worker.services.email import EmailService
from worker.services.sms import SMSService
from worker.services.websocket import WebsocketService


class BaseTask(Task):
    default_retry_delay = 60 * 5,
    max_retries = 5
    retry_backoff = True
    services = {
        'email': EmailService,
        'sms': SMSService,
        'websocket': WebsocketService
    }
    env = Environment(loader=FileSystemLoader(
        'worker/templates/email'), trim_blocks=True)
