from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://0.0.0.0:8080/realms/fastApi_realm/protocol/openid-connect/token")
