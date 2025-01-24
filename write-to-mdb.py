from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file 
load_dotenv()

# Get the MongoDB URI from the environment variable
connection_string = os.getenv("MONGODB_URI")
if not connection_string:
    raise ValueError("MONGODB_URI environment variable is not set!")

try:
    # Connect to MongoDB
    client = MongoClient(connection_string)
    
    # Select the database and collection
    db = client['learn-loop-db']
    collection = db['course_catalog']
    
    # Define the document to insert
    new_course_document = {
        "course_department": "CSE",
        "course_number": 332,
        "course_name": "Object Oriented Software Development Laboratory",
    }
    
    # Insert the document into the collection
    result = collection.insert_one(new_course_document)
    print("Document inserted with ID:", result.inserted_id)
    
except Exception as e:
    print("Failed to interact with MongoDB:", e)