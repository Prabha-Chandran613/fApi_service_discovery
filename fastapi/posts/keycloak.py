from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(os.getenv("tokenUrl"))
