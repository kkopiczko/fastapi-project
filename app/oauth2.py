from jose import JWTError, jwt

SECRET_KEY = "803e903091e47123cfe681be4804db35c4002d64507874cb951ff60e253a5917"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")