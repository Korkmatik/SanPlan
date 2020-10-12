FROM openjdk:11
ADD ./target/*-SNAPSHOT.jar /usr/src/app.jar
WORKDIR usr/src
ENTRYPOINT ["java","-jar", "app.jar"]