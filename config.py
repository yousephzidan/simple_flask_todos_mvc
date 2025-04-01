import os
from dotenv import load_dotenv

# Load env variables 
load_dotenv()

# Flask App Configuration
# https://flask.palletsprojects.com/en/stable/config/
class Config(object):
    """Base configuration"""
    DEBUG: bool = True

class Development(Config):
    SQLALCHEMY_DATABASE_URI: str = "postgresql://ysf:123@127.0.0.1:5432/todos"
    SECERT_KEY = os.getenv("SECERT_KEY")

