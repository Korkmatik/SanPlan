FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1

ADD . /code

WORKDIR /code

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add --no-cache mariadb-dev jpeg-dev openjpeg-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

RUN apk del build-deps