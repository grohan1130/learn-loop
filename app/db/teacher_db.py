from app.db.mongodb import get_mongodb_connection

def add_teacher(teacher_data):
    """Adds a teacher to the teacher_directory collection."""
    try:
        with get_mongodb_connection() as client:
            db = client['learn-loop-db']
            collection = db['teacher_directory']
            result = collection.insert_one(teacher_data)
            print("Teacher inserted with ID:", result.inserted_id)
    except Exception as e:
        print("Failed to insert teacher:", e)

def verify_login_teacher(teacher_data):
    """Verifies a teacher's login credentials."""
    try:
        with get_mongodb_connection() as client:
            db = client['learn-loop-db']
            collection = db['teacher_directory']
            teacher = collection.find_one({
                "teacher_username": teacher_data["teacher_username"],
                "teacher_password": teacher_data["teacher_password"]
            })
            return teacher if teacher else None
    except Exception as e:
        print("Failed to verify teacher login:", e)
        return None

def get_teacher_details(teacher_username):
    """Fetches a teacher's full name based on their username."""
    try:
        with get_mongodb_connection() as client:
            db = client['learn-loop-db']
            collection = db['teacher_directory']
            teacher = collection.find_one({"teacher_username": teacher_username},
                                          {"_id": 0, "teacher_first_name": 1, "teacher_last_name": 1})
            if teacher:
                return {"first_name": teacher["teacher_first_name"], "last_name": teacher["teacher_last_name"]}
            return {"first_name": "Unknown", "last_name": "Unknown"}
    except Exception as e:
        print("Failed to retrieve teacher details:", e)
        return {"first_name": "Unknown", "last_name": "Unknown"}
