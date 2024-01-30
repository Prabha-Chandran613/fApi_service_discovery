# posts
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import posts.models
from posts.database import engine, Base
import posts.posts
import posts.schema
import slack.slack
from py_eureka_client import eureka_client
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import py_eureka_client.eureka_client as eureka_client
import httpx
app = FastAPI()
your_rest_server_port = 8001

async def startup_event():
    await eureka_client.init_async(eureka_server="http://admin:admin@localhost:8761/eureka/",
                                   app_name="fastapi",
                                   instance_port=your_rest_server_port)


async def shutdown_event():
    await eureka_client.fini_async()

# Register the startup and shutdown event handlers
app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)



# Endpoint to provide Microservice 2 URL
@app.get("/get_microservice2_url")
async def get_microservice2_url():
    return {"microservice2_url": f"http://localhost:{your_rest_server_port}"}   


# posts

posts.models.Base.metadata.create_all(bind=engine)
app.include_router(posts.posts.router)

# slack
app.include_router(slack.slack.router)