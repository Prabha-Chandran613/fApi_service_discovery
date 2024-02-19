# posts
from asyncio.base_futures import _format_callbacks
from pipes import quote
from typing import Union
from fastapi import FastAPI, HTTPException, applications, logger
from pydantic import BaseModel
from typing import List
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from requests import HTTPError
import posts.models
from posts.database import engine, Base
import posts.posts
import posts.schema
# import slack.slack
from py_eureka_client import eureka_client
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import py_eureka_client.eureka_client as eureka_client
import httpx
from py_eureka_client.logger import get_logger
import os
from py_eureka_client import ERROR_REGISTER, ERROR_DISCOVER, ERROR_STATUS_UPDATE
from dotenv import load_dotenv
from py_eureka_client.eureka_basic import get_applications
import requests
import xml.etree.ElementTree as ET

load_dotenv()

app = FastAPI()


async def startup_event():
    await eureka_client.init_async(eureka_server=os.getenv("eureka_server"),
                                   app_name=os.getenv("app_name"),
                                   instance_port=int(os.getenv("microservice2_port")))


async def shutdown_event():
    await eureka_client.fini_async()

# Register the startup and shutdown event handlers
app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)





def get_microservice_url(app_name: str) -> str:
    # Make a GET request to the Eureka server to fetch the applications information
    response = requests.get(os.getenv("eureka_server_instances"))
    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.content)
        # Iterate through each application
        for application in root.findall("./application"):
            name = application.find("name").text
            if name == app_name:
                # If the application name matches, extract and return the URL of the first instance
                instance = application.find("./instance")
                home_page_url = instance.find("homePageUrl").text
                return home_page_url
        # If no matching application is found, return None
        return None
    else:
        # If the request fails, raise an exception
        raise Exception(f"Failed to fetch applications from Eureka server: {response.status_code}")

# Example usage:
    
@app.get("/get_other")
def get_other():
    microservice_url = get_microservice_url(os.getenv("other_service_name"))
    return {"url":microservice_url}




# async def get_service_url_by_name(service_name: str) -> str:
#     instances = eureka_client.do_service(service_name)
#     if instances:
#         instance = instances[0]
#         app_url = f"http://{instance.hostName}:{instance.port['$']}"
#         return app_url
#     else:
#         return None

# @app.get("/get_other")
# async def get_other_service_result():
#     other_service_name = "MICROSERVICE2"
#     other_service_context_path = "/hi"
    
#     service_url = await get_service_url_by_name(other_service_name)
#     if service_url:
#         async with httpx.AsyncClient() as client:
#          try:
#                 response = await client.get(f"{service_url}{other_service_context_path}")
#                 response.raise_for_status()
#                 return {"result_of_other_service": response.text}
#          except httpx.HTTPError as e:
#                 return {"error": f"Failed to fetch result from {other_service_name}: {str(e)}"}
#     else:
#         return {"error": f"No instances found for {other_service_name}"}



@app.get("/hii")
async def get_microservice2_url():
    return {"message": "hii....hi am prabha from microservice2"}   

# async def get_service_url_by_name():
#     app_name ="fastapi-post"
#     eureka_server = os.getenv("eureka_server")
#     print("Eureka Server:", eureka_server)
#     instances = eureka_client.get_application(app_name)
#     print("Instances:", instances)
#     if instances:
#         instance = instances[0]
#         app_url = f"http://{instance.hostName}:{instance.port['$']}"
#         return app_url
#     else:
#         return None

# # Example usage


# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())


    
    
# your_rest_server_port=int(os.getenv("microservice2_port"))
# # Endpoint to provide Microservice 2 URL
# @app.post("/get_microservice2_url")
# async def get_microservice2_url():
#     return {"hiiii"}   



# Endpoint to call Microservice 2 and get its URL
# @app.get("/")
# async def read_root():
#     try:
#         async with httpx.AsyncClient() as client:
#             response = await client.get(os.getenv("get_url_microservice1"))
#             response.raise_for_status()
#             data = response.json()
#             microservice1_url = data["microservice1_url"]
#         return {"message": f"Hello from Microservice 2! Microservice 1 URL: {microservice1_url}"}
#     except httpx.RequestError as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)
    


# posts

posts.models.Base.metadata.create_all(bind=engine)
app.include_router(posts.posts.router)

# slack
# app.include_router(slack.slack.router)