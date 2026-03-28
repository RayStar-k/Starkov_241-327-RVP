import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/lab4_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APPLICATION_ROOT = '/rvp/lab5'
    PREFERRED_URL_SCHEME = 'https'

