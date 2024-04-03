from typing import List
from fastapi import APIRouter, HTTPException,status
from fastapi.params import Body
from models.user import NewUser, UserSignIn

router = APIRouter(tags=["User"])

users={}

@router.post("/signup")
async def sign_new_user(data: NewUser) -> dict:
    if data.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User with supplied username exists")
    users[data.email] = data
    return {"message": "User successfully registered!"}

@router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User does not exist")
    if user.password != users[user.email].password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Wrong credentials passed")
    return {"message": "User signed in successfully"}




