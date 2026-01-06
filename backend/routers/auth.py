from fastapi import APIRouter, Depends, status, HTTPException
from models.auth import UserCreate
from database.session import get_db_connection, Account
from sqlalchemy.orm import Session
from database.helpers import data_exists
from pwdlib import PasswordHash

"""
Auth.py is responsible for the API that related to user signup/signin process. 
1) Create New Account
2) Login
3) Generate JWT
"""

router = APIRouter()
password_hash = PasswordHash.recommended()

@router.post("/register/")
async def create_user(user: UserCreate, db: Session = Depends(get_db_connection)):
    # Check if the email already exist in the database
    try:
        if data_exists(db, Account, email=user.email):
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Email Already Exist")
        # Hashing Password
        user.password = password_hash.hash(user.password)
        # Create a New User Class
        new_user = Account(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    except HTTPException:
        raise

