# python

This project have 3 modules :
          1. Eureka Server for Service Discovery
          2. Microservice_1  
          3. Microservice_2

         and both microservices (using fastapi) connected with postgres database.

         In .env file , give change your details Such as:
            1. microservice2_port = ****
            2. SQLALCHEMY_DATABASE_URL_DOCKER = ***************
            3. tokenUrl="http://0.0.0.0:8080/realms/*********/protocol/openid-connect/token"
            4. eureka_server="http://*****:admin@localhost:8761/eureka/" 
            5. app_name="fastapi"

    












## postgres 
docker compose -f postgresql.yml down
docker compose -f postgresql.yml up

## jhispter-resgitry 

docker compose -f jhipster-registry.yml down
docker compose -f jhipster-registry.yml up

## application 

docker compose --network=host -p8001:8001 fastapi -d  
(-d for detach mode)

