from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.params import Body
from database.connection import get_session
from models.user import NewUser, User, UserSignIn

router = APIRouter(tags=["User"])

users={}

@router.post("/signup")
async def sign_new_user(data: User, session=Depends(get_session)) -> dict:
    user = session.get(User, data.email)
    if not user:
        session.add(data)
        session.commit()
        return {"message": "user registered successfully"}
         
    raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="User with the supplied email already exists")
   

@router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    pass




