FROM python:3.9.5-slim-buster

RUN apt-get update -y && apt-get upgrade -y

WORKDIR /api

COPY ./api/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./api/src .

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh .

RUN chmod +x wait-for-it.sh

EXPOSE 8800/tcp

CMD ["gunicorn", "main:app", \
     "--workers", "4", "--worker-class", \
     "uvicorn.workers.UvicornWorker", \
     "--bind", "0.0.0.0:8800"]