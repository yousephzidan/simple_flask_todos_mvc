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
    DB_SERVER: str
    SECERT_KEY = os.getenv("SECERT_KEY")

