import bson
from app.db.mongodb import get_mongodb_connection

# Add a new course to the database
def add_course(course_data):
    """Adds a course to the course_catalog collection."""
    try:
        with get_mongodb_connection() as client:
            db = client['learn-loop-db']
            collection = db['course_catalog']

            course_department = str(course_data["course_department"]).strip().upper()
            course_number = bson.Int64(int(course_data["course_number"]))
            course_name = str(course_data["course_name"]).strip()
            teacher_username = str(course_data["teacher_username"]).strip()

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

# Retrieve all courses taught by a specific teacher
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

# Retrieve a course by its ID
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

def get_all_courses():
    """Fetches all courses from the course_catalog collection."""
    try:
        with get_mongodb_connection() as client:
            db = client["learn-loop-db"]
            course_catalog = db["course_catalog"]

            # Retrieve all courses with only necessary fields
            courses = list(course_catalog.find({}, {"_id": 0, "course_id": 1, "course_name": 1}))
            return courses
    except Exception as e:
        print("Failed to retrieve courses:", e)
        return []
