from pymongo import MongoClient
from dotenv import load_dotenv
import os
import bson

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

# Add a course to the database with correct data types
def add_course(course_data):
    connection_string = get_mongodb_connection_string()
    try:
        with MongoClient(connection_string) as client:
            db = client['learn-loop-db']
            collection = db['course_catalog']

            # Ensure correct data types
            course_department = str(course_data["course_department"]).strip().upper()
            course_number = bson.Int64(int(course_data["course_number"]))  # Enforce int64
            course_name = str(course_data["course_name"]).strip()
            teacher_username = str(course_data["teacher_username"]).strip()

            # Generate course_id properly
            course_id = f"{course_department}{course_number}"  # Example: "CSE330"

            course_document = {
                "course_department": course_department,
                "course_number": course_number,
                "course_name": course_name,
                "course_id": course_id,  # Corrected ID format
                "teacher_username": teacher_username
            }

            result = collection.insert_one(course_document)
            print(f"Course inserted with ID: {result.inserted_id}")

    except Exception as e:
        print("Failed to insert course into MongoDB:", e)

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

# Function to get courses taught by a specific teacher
def get_courses_by_teacher(teacher_username):
    connection_string = get_mongodb_connection_string()
    try:
        with MongoClient(connection_string) as client:
            db = client['learn-loop-db']
            collection = db['course_catalog']

            # Query courses by teacher username
            courses = list(collection.find({"teacher_username": teacher_username}))

            # Convert MongoDB ObjectId to string
            for course in courses:
                course["_id"] = str(course["_id"])

            return courses
    except Exception as e:
        print("Failed to retrieve courses from MongoDB:", e)
        return []