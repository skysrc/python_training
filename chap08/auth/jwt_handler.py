import time 
from datetime import datetime,timezone
from fastapi import HTTPException, status
from jose import jwt, JWTError
import os
from dotenv import load_dotenv

load_dotenv()

def create_access_token(user: str) -> str:
    payload = {
        "user" : user,
        "expire": time.time() + 3600 # in seconds thus 1 hr
    }

    token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")
    return token

def verify_access_token(token: str) -> dict:
    try:
        # if successfully decode, return dict of ori data
        data = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        expire = data.get("expire")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="no access token supplied")

        if datetime.now(timezone.utc) > datetime.fromtimestamp(expire, timezone.utc):
            #expired 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Invalid token")
        #everything ok
        return data
    except JWTError:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Invalid token")