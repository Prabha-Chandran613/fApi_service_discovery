# eureka_server.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Eureka Server"}



# docker command for run the eureka server 
# docker compose -f jhipster-registry.yml up     