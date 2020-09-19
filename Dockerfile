FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY web/ /code

RUN pip3 install -r /code/requirements.txt

