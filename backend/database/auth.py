from .session import get_db_connection
from sqlalchemy import insert
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def hashed_password(plained_password):
    return password_hash.hash(plained_password)

def verify_password(plained_password, stored_password):
    return password_hash.verify(plained_password, stored_password)



    
