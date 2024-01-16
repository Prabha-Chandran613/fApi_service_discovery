from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import models
from database import engine, Base
import posts
import schema

app = FastAPI()

# #this is for Keycloak integration 
# # we just provide token URL and install pip install python-multipart
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8080/realms/djangorealm/protocol/openid-connect/token")

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get("/")
# # for every api we need to add "async" and (token: str = Depends(oauth2_scheme)) for every API to Authenticate
# async def read_root(token: str = Depends(oauth2_scheme)):
#     return {"token": "hi"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None, token: str = Depends(oauth2_scheme)):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, token: str = Depends(oauth2_scheme)):
#     return {"item_name": item.name, "item_id": item_id}


models.Base.metadata.create_all(bind=engine)
app.include_router(posts.router)