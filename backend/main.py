from fastapi import FastAPI
from routers import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(auth.router)

allowed_orgin = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_orgin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Finance Tracker Application"}