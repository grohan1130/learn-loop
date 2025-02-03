from pymongo import MongoClient
from dotenv import load_dotenv
import os

def get_mongodb_connection():
    """Returns a MongoDB client connection."""
    load_dotenv()
    connection_string = os.getenv("MONGODB_URI")
    if not connection_string:
        raise ValueError("MONGODB_URI environment variable is not set!")
    
    return MongoClient(connection_string)
