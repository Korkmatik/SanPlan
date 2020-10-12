<<<<<<< HEAD
FROM openjdk:11
ADD ./target/*-SNAPSHOT.jar /usr/src/app.jar
WORKDIR usr/src
ENTRYPOINT ["java","-jar", "app.jar"]
=======
FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY web/ /code

RUN pip3 install -r /code/requirements.txt

>>>>>>> parent of d990153... Removed Django Project
