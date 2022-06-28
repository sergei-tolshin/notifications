import logging

import uvicorn
from celery import Celery
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import notices
from core import config
from core import logger as logger_config
from db import message_broker

logger = logging.getLogger(__name__)

app = FastAPI(
    title='Notice API для онлайн-кинотеатра',
    description=('API для приёма событий по созданию уведомлений'),
    version='1.0.0',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    redoc_url='/api/redoc',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    message_broker.producer = Celery(
        'senders',
        broker=config.CELERY_BROKER_URL,
        backend=config.CELERY_RESULT_BACKEND,
        database_table_schemas={
            'task': 'notice',
            'group': 'notice',
        }
    )


@app.on_event('shutdown')
async def shutdown():
    pass


app.include_router(notices.router, prefix='/api/v1/notices',
                   tags=['Отправка уведомлений'])


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_config=logger_config.LOGGING,
        log_level=logging.DEBUG,
    )
