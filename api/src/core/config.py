import os
from logging import config as logging_config
from pathlib import Path

from core.logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)

# Название проекта. Используется в Swagger-документации
PROJECT_NAME = os.getenv('PROJECT_NAME', 'notice_app')

# RabbitMQ
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'amqp://localhost')
CELERY_RESULT_BACKEND = os.getenv(
    'CELERY_RESULT_BACKEND',
    'db+postgresql://app:123qwe@localhost/notice_database'
)

# Корень проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Локализация
LANGUAGE = os.getenv('LANGUAGE', 'ru')
LOCALE_PATH = os.getenv('LOCALE_PATH', 'locale')
