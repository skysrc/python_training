from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.params import Body
from auth.jwt_handler import create_access_token
from database.connection import get_session
from models.user import NewUser, User, UserSignIn
from fastapi.security import OAuth2PasswordRequestForm # html form to login
from auth.hash_password import HashPassword

router = APIRouter(tags=["User"])

users={}

@router.post("/signup")
async def sign_new_user(data: User, session=Depends(get_session)) -> dict:
    user = session.get(User, data.email)
    if not user:
        hp = HashPassword()
        data.password = hp.create_hash(data.password)
        session.add(data)
        session.commit()
        return {"message": "user registered successfully"}
         
    raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="User with the supplied email already exists")
   

@router.post("/signin")
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)) -> dict:
    user_exists = session.get(User, user.username)
    if user_exists:
        hashed_password = HashPassword()
        if hashed_password.verify_hash(user.password, user_exists.password):
            #password matched
            access_token = create_access_token(user_exists.email)
            return {"access_token": access_token,
                    "token_type": "Bearer"}
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail="Invalid credential")




