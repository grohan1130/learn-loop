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
        with MongoClient(connection_string) as client:
            db = client['learn-loop-db']
            collection = db['student_body']
            result = collection.insert_one(student_data)
            print("Document inserted with ID:", result.inserted_id)
    except Exception as e:
        print("Failed to interact with MongoDB:", e)

# Add to teacher_directory database
def add_teacher(teacher_data):
    connection_string = get_mongodb_connection_string()
    try:
        with MongoClient(connection_string) as client:
            db = client['learn-loop-db']
            collection = db['teacher_directory']
            result = collection.insert_one(teacher_data)
            print("Document inserted with ID:", result.inserted_id)
    except Exception as e:
        print("Failed to interact with MongoDB:", e)

# Add to course_catalog database
def add_course(course_data):
    connection_string = get_mongodb_connection_string()
    try:
        with MongoClient(connection_string) as client:
            db = client['learn-loop-db']
            collection = db['course_catalog']
            result = collection.insert_one(course_data)
            print("Document inserted with ID:", result.inserted_id)
    except Exception as e:
        print("Failed to interact with MongoDB:", e)

# login teacher (verify username/password credentials)
def verify_login_teacher(teacher_data):
    connection_string = get_mongodb_connection_string()
    try:
        with MongoClient(connection_string) as client:
            db = client['learn-loop-db']
            collection = db['teacher_directory']

            query = {
                "teacher_username": teacher_data["teacher_username"],
                "teacher_password": teacher_data["teacher_password"]
            }

            teacher = collection.find_one(query)  # Fetch full teacher record
            return teacher if teacher else None  # Return dictionary or None
    except Exception as e:
        print("Failed to interact with MongoDB:", e)
        return None  # Return None if there's an exception

# login student (verify username/password credentials)
def verify_login_student(student_data):
    connection_string = get_mongodb_connection_string()
    try:
        with MongoClient(connection_string) as client:
            db = client['learn-loop-db']
            collection = db['student_body']

            query = {
                "student_username": student_data["student_username"],
                "student_password": student_data["student_password"]
            }

            student = collection.find_one(query)  # Fetch full student record
            return student if student else None  # Return dictionary or None
    except Exception as e:
        print("Failed to interact with MongoDB:", e)
        return None  # Return None if there's an exception
