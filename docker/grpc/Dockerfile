FROM python:3.9.5-slim-buster
RUN apt-get update -y && apt-get upgrade -y
WORKDIR /grpc
COPY ./grpc_fake/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./grpc_fake .
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh .
RUN chmod +x wait-for-it.sh

CMD [ "python", "server.py" ]