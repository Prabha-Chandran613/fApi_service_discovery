# Use an OpenJDK runtime as a base image
FROM openjdk:11-jre-slim


WORKDIR /app


COPY ./src/main/java/com/fastApi/eurekaserver/EurekaServerApplication.java /app/

COPY ./target/eureka-server-0.0.1-SNAPSHOT.jar /app/app.jar


EXPOSE 8761

ENTRYPOINT ["java", "-jar", "app.jar"]
