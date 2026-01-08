from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta
from config.setting import Settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException, status

password_hash = PasswordHash.recommended()

def hashed_password(plained_password):
    return password_hash.hash(plained_password)

def verify_password(plained_password, stored_password):
    return password_hash.verify(plained_password, stored_password)

def jwt_encode(user_id, refresh_time: int, secret_key, encoding_algorithm: str='HS256'):

    payload = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + timedelta(minutes=refresh_time),
        "iat":  datetime.utcnow()
    }

    econded_jwt = jwt.encode(payload, secret_key, encoding_algorithm)
    return econded_jwt


def verify_jwt_signature(token, secret_key, encoding_algorithm: str='HS256') -> dict:
    try:
        payload = jwt.decode(token, secret_key, encoding_algorithm)
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,detail="Token Has Expired")
    except InvalidTokenError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Token Error: {e}")