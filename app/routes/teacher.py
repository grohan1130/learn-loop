from flask import Blueprint, render_template, session, redirect, url_for, request
from app.db.teacher_db import get_teacher_details
from app.db.enrollment_db import get_students_in_course
from app.db.course_db import add_course as add_course_to_db, get_courses_by_teacher, get_course_by_id


teacher = Blueprint("teacher", __name__)

# Teacher Dashboard - Shows courses the teacher teaches
@teacher.route("/teacher-dashboard")
def teacher_dashboard():
    if "teacher_username" not in session:
        return redirect(url_for("auth.login_teacher"))

    courses = get_courses_by_teacher(session["teacher_username"])
    teacher_details = get_teacher_details(session["teacher_username"])

    return render_template("teacher-dashboard.html", 
                           first_name=teacher_details["first_name"], 
                           last_name=teacher_details["last_name"], 
                           courses=courses)

# Course Page for a Teacher
@teacher.route("/course/<course_id>")
def course_page(course_id):
    if "teacher_username" not in session:
        return redirect(url_for("auth.login_teacher"))

    course = get_course_by_id(course_id)
    if not course:
        return "<h1>Course not found</h1>", 404

    students = get_students_in_course(course_id)
    teacher_details = get_teacher_details(session["teacher_username"])

    return render_template("teacher-course-page.html", 
                           course=course, 
                           students=students,
                           first_name=teacher_details["first_name"], 
                           last_name=teacher_details["last_name"])

@teacher.route("/add-course", methods=["POST"])
def add_course():
    if "teacher_username" not in session:
        return redirect(url_for("auth.login_teacher"))

    department = request.form.get("department").strip().upper()
    number = request.form.get("number").strip()
    name = request.form.get("name").strip()

    if not (department and number and name):
        return redirect(url_for("teacher.teacher_dashboard"))

    course_data = {
        "course_department": department,
        "course_number": int(number),
        "course_name": name,
        "teacher_username": session["teacher_username"]
    }
    
    add_course_to_db(course_data)  # ✅ Now calling the correct function
    
    return redirect(url_for("teacher.teacher_dashboard"))

