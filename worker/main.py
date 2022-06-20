from celery import Celery

import config


app = Celery(__name__, include=['tasks'])
app.config_from_object(config)
