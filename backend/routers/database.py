from fastapi import APIRouter, HTTPException
from database.session import create_table

router = APIRouter(prefix="/database")

@router.post("/setup")
async def setup():
    try:
        create_table()
        return {"status": "ok", "message": "Tables ensured"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Database setup failed"
        )