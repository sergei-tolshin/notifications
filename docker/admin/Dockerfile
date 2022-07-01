ARG COMPOSE_PROJECT_NAME=notifications
FROM ${COMPOSE_PROJECT_NAME}_base

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh .
RUN chmod +x wait-for-it.sh

COPY docker/admin/entrypoint.sh  /app/docker/admin/