FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1

ADD . /code

WORKDIR /code

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install
