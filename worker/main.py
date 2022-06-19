from celery import Celery

import config


app = Celery(__name__, include=['tasks'])
app.config_from_object(config)

app.conf.beat_schedule = {
    'run-me-every-ten-seconds': {
        'task': 'tasks.check',
        'schedule': 10.0,
    }
}
