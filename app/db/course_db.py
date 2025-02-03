import bson
from app.db.mongodb import get_mongodb_connection

def add_course(course_data):
    """Adds a course to the course_catalog collection with correct data types."""
    try:
        with get_mongodb_connection() as client:
            db = client['learn-loop-db']
            collection = db['course_catalog']

            # Ensure correct data types
            course_department = str(course_data["course_department"]).strip().upper()
            course_number = bson.Int64(int(course_data["course_number"]))  # Enforce int64
            course_name = str(course_data["course_name"]).strip()
            teacher_username = str(course_data["teacher_username"]).strip()

            # Generate course_id
            course_id = f"{course_department}{course_number}"

            course_document = {
                "course_department": course_department,
                "course_number": course_number,
                "course_name": course_name,
                "course_id": course_id,
                "teacher_username": teacher_username
            }

            result = collection.insert_one(course_document)
            print(f"Course inserted with ID: {result.inserted_id}")
    except Exception as e:
        print("Failed to insert course:", e)

def get_courses_by_teacher(teacher_username):
    """Retrieves all courses taught by a specific teacher."""
    try:
        with get_mongodb_connection() as client:
            db = client['learn-loop-db']
            collection = db['course_catalog']
            courses = list(collection.find({"teacher_username": teacher_username}))
            for course in courses:
                course["_id"] = str(course["_id"])
            return courses
    except Exception as e:
        print("Failed to retrieve courses:", e)
        return []

def get_course_by_id(course_id):
    """Fetches a course by its ID."""
    try:
        with get_mongodb_connection() as client:
            db = client['learn-loop-db']
            collection = db['course_catalog']
            course = collection.find_one({"course_id": course_id}, {"_id": 0})
            return course
    except Exception as e:
        print("Failed to retrieve course details:", e)
        return None
