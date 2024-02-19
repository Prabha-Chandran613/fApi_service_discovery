from fastapi import FastAPI
import os
import models
from database import engine
import posts
from py_eureka_client import eureka_client
from dotenv import load_dotenv
import asyncio
import requests
import xml.etree.ElementTree as ET

asyncio.set_event_loop(asyncio.new_event_loop())

load_dotenv()

app = FastAPI()


async def startup_event():
    await eureka_client.init_async(
        eureka_server=os.getenv("eureka_server"),
        app_name=os.getenv("app_name"),
        instance_port=int(os.getenv("microservice1_port"))
    )


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


@app.get("/hi")
async def get_microservice2_url():
    return {"message": "hii....hi am prabha from microservice1"}   

models.Base.metadata.create_all(bind=engine)
app.include_router(posts.router)



























# from fastapi import FastAPI, HTTPException
# import httpx
# import os
# import models
# from database import engine
# import posts
# from py_eureka_client import eureka_client
# from fastapi.responses import JSONResponse
# import py_eureka_client.eureka_client as eureka_client
# from dotenv import load_dotenv
# from urllib.request import HTTPError
# import http.client
# load_dotenv()

# app = FastAPI()




# async def startup_event():
#     await eureka_client.init_async(eureka_server=os.getenv("eureka_server"),
#                                    app_name=os.getenv("app_name"),
#                                    instance_port=int(os.getenv("microservice1_port")))



# async def shutdown_event():
#     await eureka_client.fini_async()



# # Register the startup and shutdown event handlers
# app.add_event_handler("startup", startup_event)
# app.add_event_handler("shutdown", shutdown_event)

# # async def get_service_url_by_name(service_name: str) -> str:
# #     instances = eureka_client.do_service(service_name)
# #     if instances:
# #         instance = instances[0]
# #         app_url = f"http://{instance.hostName}:{instance.port['$']}"
# #         return app_url
# #     else:
# #         return None

# # @app.get("/get_other")
# # async def get_other_service_result():
# #     other_service_name = "MICROSERVICE2"
# #     other_service_context_path = "/hii"
    
# #     service_url = await get_service_url_by_name(other_service_name)
# #     if service_url:
# #         async with httpx.AsyncClient() as client:
# #          try:
# #                 response = await client.get(f"{service_url}{other_service_context_path}")
# #                 response.raise_for_status()
# #                 return {"result_of_other_service": response.text}
# #          except httpx.HTTPError as e:
# #                 return {"error": f"Failed to fetch result from {other_service_name}: {str(e)}"}
# #     else:
# #         return {"error": f"No instances found for {other_service_name}"}



# @app.get("/hii")
# async def hii():
#     try:
#         # Fetch the instances of MICROSERVICE2 from the service registry
#         instances = await eureka_client.do_service("MICROSERVICE2" , "/hii")
#         if instances:
#             # Get the URL of the first instance (assuming only one instance is registered)
#             instance_url = instances[0].homePageUrl
#             return {"result_of_other_service": instance_url}
#         else:
#             raise HTTPException(status_code=404, detail="No instances found for MICROSERVICE2")
#     except Exception as e:
#         # Catch any exception and return an HTTP 500 error with the error message
#         raise HTTPException(status_code=500, detail=f"Error fetching result from MICROSERVICE2: {str(e)}")
   
   
#     # app_name = os.getenv("app_name")
#     # eureka_server = os.getenv("eureka_server")
# # @app.get("/hii")
# # async def hii():
# #     try:
# #         # print("message tested")
# #         res = await eureka_client.do_service(app_name="MICROSERVICE2", service="/hii", prefer_ip=True)
# #         return {"result_of_other_service": res}
# #     except HTTPError as e:
# #         # If all nodes are down, an `HTTPError` will be raised.
# #         # Return an HTTP 500 error indicating that something went wrong.
# #         raise HTTPException(status_code=500, detail=f"Error fetching result from MICROSERVICE2: {str(e)}")
# #     # connection = http.client.HTTPConnection("http://localhost:8761/eureka/apps", 80, timeout=10)
# #     # print(connection)

# # @app.get("/")
# # async def get_service_url_by_name():
# #     app_name = "fastapi"
# #     eureka_server = os.getenv("eureka_server")
# #     print("Eureka Server:", eureka_client)
# #     instances = eureka_client.do_service(app_name,"get_microservice2_url")
# #     print(instances)
# #     print("Instances:", instances)
# #     if instances:
# #         instan/hice = instances[0]
# #         app_url = f"http://{instance.hostName}:{instance.port['$']}"
# #         return app_url
# #     else:
# #         return None

# # # Example usage
# # async def main():

# #     service_url = await get_service_url_by_name()
# #     if service_url:
# #         print(f"Service URL: {service_url}")
# #     else:
# #         print("No instances found for the specified app name")

# # if __name__ == "__main__":
# #     import asyncio
# #     asyncio.run(main())

     

# # # Endpoint to provide Microservice 2 URL
# # @app.get("/hi")
# # async def get_microservice2_url():
# #     return {"message": "hii"}   


# # Endpoint to call Microservice 2 and get its URL
# # @app.get("/")
# # async def read_root():
# #     try:
# #         async with httpx.AsyncClient() as client:
# #             response = await client.get(os.getenv("get_url_microservice2"))
# #             response.raise_for_status()
# #             data = response.json()
# #             microservice2_url = data["microservice2_url"]
# #         return {"message": f"Hello from Microservice 1! Microservice 2 URL: {microservice2_url}"}
# #     except httpx.RequestError as e:
# #         return JSONResponse(content={"error": str(e)}, status_code=500)
    

# # eureka_client.init(eureka_server="http://localhost:8761/eureka/apps", app_name="fastapi-post")


# # The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
# # async def init_eureka_client():
# #     await asyncio.sleep(0.1)  # Introduce a small delay to allow FastAPI to set up its event loop
# #     await eureka_client.init_async()

# # # Register Eureka client before the server starts
# # @app.on_event("startup")
# # async def startup_event():
# #     asyncio.create_task(init_eureka_client())

# # # Unregister Eureka client before the server stops
# # @app.on_event("shutdown")
# # async def shutdown_event():
# #     await eureka_client.fini_async()






# # #this is for Keycloak integration 
# # # we just provide token URL and install pip install python-multipart
# # oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8080/realms/djangorealm/protocol/openid-connect/token")

# # class Item(BaseModel):
# #     name: str
# #     price: float
# #     is_offer: Union[bool, None] = None

# # @app.get("/")
# # # for every api we need to add "async" and (token: str = Depends(oauth2_scheme)) for every API to Authenticate
# # async def read_root(token: str = Depends(oauth2_scheme)):
# #     return {"token": "hi"}

# # @app.get("/items/{item_id}")
# # async def read_item(item_id: int, q: Union[str, None] = None, token: str = Depends(oauth2_scheme)):
# #     return {"item_id": item_id, "q": q}

# # @app.put("/items/{item_id}")
# # async def update_item(item_id: int, item: Item, token: str = Depends(oauth2_scheme)):
# #     return {"item_name": item.name, "item_id": item_id}


# # # Register with JHipster Registry
# # jhipster_registry_url = "http://localhost:8761/eureka/apps"
# # microservice_name = "fastapi-post"

# # requests.post(
# #     f"{jhipster_registry_url}/apps/{microservice_name}",
# #     json={
# #         "instance": {
# #             "hostName": "fastapi-post",
# #             "app": "fastapi-post",
# #             "ipAddr": "localhost",
# #             "status": "UP",
# #             "port": {"$": 8000, "@enabled": "true"},
# #             "vipAddress": "fastapi-post",
# #             "secureVipAddress": "fastapi-post",
# #             "dataCenterInfo": {"@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo", "name": "MyOwn"},
# #         }
# #     },
# # )

# models.Base.metadata.create_all(bind=engine)
# app.include_router(posts.router)