FROM python:3.9.5-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /admin

COPY ./admin/requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY ./admin/ .

EXPOSE 8080/tcp

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh .
RUN chmod +x wait-for-it.sh

CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8080" ]