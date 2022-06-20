import json
import os


broker_url = os.environ.get('CELERY_BROKER_URL', 'amqp://localhost')
result_backend = os.environ.get(
    'CELERY_RESULT_BACKEND',
    'db+postgresql://app:123qwe@localhost/notice_database'
)
database_table_schemas = {
    'task': 'notice',
    'group': 'notice',
}
result_extended = True
timezone = 'Europe/Moscow'
enable_utc = True
