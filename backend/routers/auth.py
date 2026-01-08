from fastapi import APIRouter, Depends, status, HTTPException
from models.auth import UserCreate, UserRetreive, UserLogin
from database.session import get_db_connection, Account
from sqlalchemy.orm import Session
from database.helpers import data_exists
from utils.security import hashed_password, verify_password, jwt_encode, verify_jwt_signature
from config.setting import Settings

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
async def login(payload: UserLogin, db: Session = Depends(get_db_connection)):
    # Get the User Account
    user = db.query(Account).filter(Account.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Invalid Email or Password")
    # Generate a return jwt token
    access_token = jwt_encode(user.id, 5, Settings.JWT_SECRET_KEY) 
    return {"access_token": access_token, "token_type": "bearer"}