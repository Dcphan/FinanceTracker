from fastapi import FastAPI
from routers import auth, database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

routers = [
    auth.router,
    database.router
]

for router in routers:
    app.include_router(router)

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