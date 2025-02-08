from app.db.mongodb import get_mongodb_connection
from datetime import datetime

def enroll_student_in_course(student_username, course_id):
    try:
        with get_mongodb_connection() as client:
            db = client["learn-loop-db"]
            course_roster = db["course_roster"]

            existing_enrollment = course_roster.find_one({"student_username": student_username, "course_id": course_id})

            if existing_enrollment:
                return False  

            enrollment_data = {
                "student_username": student_username,
                "course_id": course_id,
                "enrolled_at": datetime.utcnow()
            }
            course_roster.insert_one(enrollment_data)
            return True  

    except Exception as e:
        return False


def get_student_courses(student_username):
    try:
        with get_mongodb_connection() as client:
            db = client["learn-loop-db"]
            course_roster = db["course_roster"]
            course_catalog = db["course_catalog"]

            enrolled_courses = list(course_roster.find({"student_username": student_username}, {"_id": 0, "course_id": 1}))
            course_ids = [entry["course_id"] for entry in enrolled_courses]
            courses = list(course_catalog.find({"course_id": {"$in": course_ids}}, {"_id": 0, "course_id": 1, "course_name": 1}))

            return courses
    except Exception as e:
        return []


def get_students_in_course(course_id):
    try:
        with get_mongodb_connection() as client:
            db = client["learn-loop-db"]
            course_roster = db["course_roster"]
            student_body = db["student_body"]

            enrolled_students = list(course_roster.find({"course_id": course_id}, {"_id": 0, "student_username": 1}))
            student_usernames = [entry["student_username"] for entry in enrolled_students]
            students = list(student_body.find({"student_username": {"$in": student_usernames}}, {"_id": 0, "student_first_name": 1, "student_last_name": 1}))

            return students
    except Exception as e:
        return []
