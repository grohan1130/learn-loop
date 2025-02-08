from flask import Blueprint, render_template, session, redirect, url_for, request
from app.db.enrollment_db import enroll_student_in_course, get_student_courses
from app.db.course_db import get_all_courses, get_course_by_id
from app.db.teacher_db import get_teacher_details

student = Blueprint("student", __name__)

# Student Dashboard
@student.route("/student-dashboard")
def student_dashboard():
    if "student_username" not in session:
        return redirect(url_for("auth.login_student"))

    available_courses = get_all_courses()
    enrolled_courses = get_student_courses(session["student_username"])

    return render_template("student-dashboard.html", 
                           first_name=session["student_first_name"], 
                           available_courses=available_courses,
                           enrolled_courses=enrolled_courses)

# Enroll in a Course
@student.route("/enroll-course", methods=["POST"])
def enroll_course():
    if "student_username" not in session:
        return redirect(url_for("auth.login_student"))

    course_id = request.form.get("course_id")

    if not course_id:
        return redirect(url_for("student.student_dashboard"))

    enroll_student_in_course(session["student_username"], course_id)
    return redirect(url_for("student.student_dashboard"))

# Course Page for Students
@student.route("/course/<course_id>")
def student_course_page(course_id):
    if "student_username" not in session:
        return redirect(url_for("auth.login_student"))

    course = get_course_by_id(course_id)
    if not course:
        return "<h1>Course not found</h1>", 404

    instructor = get_teacher_details(course["teacher_username"])

    return render_template("student-course-page.html", 
                           course=course, 
                           instructor=instructor)
