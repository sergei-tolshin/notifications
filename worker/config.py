import json
import os


broker_url = os.environ.get('CELERY_BROKER_URL', 'amqp://rabbitmq')
result_backend = os.environ.get(
    'CELERY_RESULT_BACKEND',
    'db+postgresql://app:123qwe@postgres/notice_database'
)
# database_engine_options = json.loads(
#     os.environ.get(
#         'CELERY_RESULT_ENGINE_OPTIONS',
#         '{"connect_args": {"options": "-csearch_path=notice"}}'
#     )
# )
database_table_schemas = {
    'task': 'notice',
    'group': 'notice',
}
enable_utc = True
