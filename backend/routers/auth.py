from fastapi import APIRouter, Depends, status, HTTPException, Response
from models.auth import UserCreate, UserRetreive, UserLogin
from database.session import get_db_connection, Account, SessionStorage
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.helpers import data_exists
from database.auth import insert_refresh_token
from utils.security import hashed_password, verify_password, jwt_encode, verify_jwt_signature
from config.setting import Settings
import secrets

"""
Auth.py is responsible for the API that related to user signup/signin process. 
1) Create New Account
2) Login
3) Generate JWT
"""

router = APIRouter(prefix="/auth")

@router.post("/register/")
async def create_user(user: UserCreate, db: Session = Depends(get_db_connection)):
    # Check if the email already exist in the database
    if data_exists(db, Account, email=user.email):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Email Already Exist")
    
    # Hashing Password
    user.password_hash = hashed_password(user.password_hash)
    
    # Create a New User Class
    new_user = Account(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
async def login(response: Response, payload: UserLogin, db: Session = Depends(get_db_connection)):
    ACCESS_TOKEN_TIME = 5
    REFRESH_TOKEN_TIME = 15
    # Get the User Account
    user = db.query(Account).filter(Account.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Invalid Email or Password")
    
    # Generate Token for Authentication    
    access_token = jwt_encode(user.id, ACCESS_TOKEN_TIME, Settings.JWT_SECRET_KEY) 
    refresh_token = jwt_encode(user.id, REFRESH_TOKEN_TIME, Settings.JWT_SECRET_KEY)

    # If User already exist in jwt token then change it, else add it in 
    insert_refresh_token(db, user.id, hashed_password(refresh_token), REFRESH_TOKEN_TIME)

    response.set_cookie(key="refresh_token", value=refresh_token, httponly= True)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/refresh")
async def refresh(request):
    print(request)