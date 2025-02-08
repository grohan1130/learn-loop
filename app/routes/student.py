from flask import Blueprint, render_template, session, redirect, url_for, request
from app.db.enrollment_db import enroll_student_in_course, get_student_courses
from app.db.course_db import get_all_courses  

student = Blueprint("student", __name__)

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


@student.route("/enroll-course", methods=["POST"])
def enroll_course():
    if "student_username" not in session:
        return redirect(url_for("auth.login_student"))

    course_id = request.form.get("course_id")

    enroll_student_in_course(session["student_username"], course_id)
    return redirect(url_for("student.student_dashboard"))
