from app.db.mongodb import get_mongodb_connection

def add_student(student_data):
    """Adds a student to the student_body collection."""
    try:
        with get_mongodb_connection() as client:
            db = client['learn-loop-db']
            collection = db['student_body']
            result = collection.insert_one(student_data)
            print("Student inserted with ID:", result.inserted_id)
    except Exception as e:
        print("Failed to insert student:", e)

def verify_login_student(student_data):
    """Verifies a student's login credentials."""
    try:
        with get_mongodb_connection() as client:
            db = client['learn-loop-db']
            collection = db['student_body']
            student = collection.find_one({
                "student_username": student_data["student_username"],
                "student_password": student_data["student_password"]
            })
            return student if student else None
    except Exception as e:
        print("Failed to verify student login:", e)
        return None
