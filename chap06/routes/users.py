from typing import List
from fastapi import APIRouter, HTTPException,status
from fastapi.params import Body
from database.connection import getConnection
from models.user import NewUser, UserSignIn

router = APIRouter(tags=["User"])

users={}

@router.post("/signup")
async def sign_new_user(data: NewUser) -> dict:
    conn = getConnection()
    sqlCheck = f"""SELECT * FROM user WHERE email = '{data.email}'"""
    cursor = conn.cursor()
    cursor.execute(sqlCheck)
    row = cursor.fetchone()
    if row:
         raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="User with the supplied email already exists")
   
    sql = f"""
        INSERT INTO user (email,password, title)
        VALUES('{data.email}','{data.password}', '{data.title}')
        """
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
        
    # if data.email in users:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User with supplied username exists")
    # users[data.email] = data
    return {"message": "User successfully registered!"}

@router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    conn = getConnection()
    sqlCheck = f"""SELECT * FROM user WHERE email = '{user.email}' AND password = '{user.password}'"""
    cursor = conn.cursor()
    cursor.execute(sqlCheck)
    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    if row is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Invalid credentials passed.")
    else:
        return {"message": "you signed in successfully"}




