from flask import Blueprint, render_template, request, redirect, url_for, session
from app.db.course_db import add_course, get_courses_by_teacher, get_course_by_id
from app.db.teacher_db import get_teacher_details

teacher = Blueprint("teacher", __name__)

# Teacher Dashboard (Displays courses taught by the teacher)
@teacher.route("/teacher-dashboard")
def teacher_dashboard():
    if "teacher_username" not in session:
        return redirect(url_for("auth.login_teacher"))

    # Fetch courses taught by the logged-in teacher
    courses = get_courses_by_teacher(session["teacher_username"])

    return render_template("teacher-dashboard.html", first_name=session["teacher_first_name"], courses=courses)


# Register Course (Only for logged-in teachers)
@teacher.route("/register-course", methods=["GET", "POST"])
def register_course():
    if "teacher_username" not in session:
        return redirect(url_for("auth.login_teacher"))

    if request.method == "POST":
        department = request.form.get("department").strip().upper()
        number = request.form.get("number").strip()
        name = request.form.get("name").strip()

        if not (department and number and name):
            print("All fields are required!", "error")
            return redirect(url_for("teacher.register_course"))

        # Construct course_id properly
        course_id = f"{department}{number}"

        course_data = {
            "course_department": department,
            "course_number": int(number),  # Ensure number is stored as an integer
            "course_name": name,
            "course_id": course_id,  # Ensure correct course ID format
            "teacher_username": session["teacher_username"]
        }
        add_course(course_data)

        return redirect(url_for("teacher.teacher_dashboard"))

    return render_template("register-course.html", teacher_username=session["teacher_username"])


# Course Page - Displays details of a selected course (Teacher View)
@teacher.route("/course/<course_id>")
def course_page(course_id):
    if "teacher_username" not in session:
        return redirect(url_for("auth.login_teacher"))

    # Fetch the course details for this specific course
    course = get_course_by_id(course_id)

    if not course:
        return "<h1>Course not found</h1>", 404  # Display 404 if course is not found

    # Fetch teacher details (first and last name)
    teacher_details = get_teacher_details(session["teacher_username"])

    return render_template("teacher-course-page.html", 
                           course=course, 
                           first_name=teacher_details["first_name"], 
                           last_name=teacher_details["last_name"])
