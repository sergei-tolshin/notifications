# FROM python:3.9.5-slim-buster

# WORKDIR /worker

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN pip install --upgrade pip
# COPY ./worker/requirements.txt .
# RUN pip install -r requirements.txt

# COPY ./worker/src .
ARG COMPOSE_PROJECT_NAME=notifications
FROM ${COMPOSE_PROJECT_NAME}_base

COPY docker/worker/entrypoint.sh  /app/docker/worker/