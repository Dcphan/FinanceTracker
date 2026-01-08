from dotenv import load_dotenv
import os

load_dotenv()  # load once

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL") 
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")