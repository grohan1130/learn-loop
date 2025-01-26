from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Get the MongoDB URI from the environment variable
def get_mongodb_connection_string():
    load_dotenv()
    connection_string = os.getenv("MONGODB_URI")
    if not connection_string:
        raise ValueError("MONGODB_URI environment variable is not set!")
    return connection_string

# Add to student_body database
def add_student(student_data):
    connection_string = get_mongodb_connection_string()
    try:
        # Connect to MongoDB
        client = MongoClient(connection_string)
        
        # Select the database and collection
        db = client['learn-loop-db']
        collection = db['student_body']
        
        # Insert the document into the collection
        result = collection.insert_one(student_data)
        print(student_data)
        print("Document inserted with ID:", result.inserted_id)
    
    except Exception as e:
        print("Failed to interact with MongoDB:", e)

# Add to teacher_directory database
def add_teacher(teacher_data):
    connection_string = get_mongodb_connection_string()
    try:
        # Connect to MongoDB
        client = MongoClient(connection_string)
        
        # Select the database and collection
        db = client['learn-loop-db']
        collection = db['teacher_directory']
        
        # Insert the document into the collection
        result = collection.insert_one(teacher_data)
        print(teacher_data)
        print("Document inserted with ID:", result.inserted_id)
    except Exception as e:
        print("Failed to interact with MongoDB:", e)

# Add to course_catalog database
def add_course(course_data):
    connection_string = get_mongodb_connection_string()
    try:
        # Connect to MongoDB
        client = MongoClient(connection_string)
        
        # Select the database and collection
        db = client['learn-loop-db']
        collection = db['course_catalog']
        
        # Insert the document into the collection
        result = collection.insert_one(course_data)
        print(course_data)
        print("Document inserted with ID:", result.inserted_id)
    except Exception as e:
        print("Failed to interact with MongoDB:", e)

# login teacher (verify username/password credentials)
def verify_login_teacher(teacher_data):
    connection_string = get_mongodb_connection_string()
    try:
        # Connect to MongoDB
        client = MongoClient(connection_string)
        
        # Select the database and collection
        db = client['learn-loop-db']
        collection = db['teacher_directory']

        query = {
            "teacher_username": teacher_data["teacher_username"],
            "teacher_password": teacher_data["teacher_password"]
        }
        
        # Check if the user exists
        return collection.find_one(query) is not None

    except Exception as e:
        print("Failed to interact with MongoDB:", e)
        return False  # Return False if there's an exception

    finally:
        # Close the MongoDB client connection
        client.close()

    

