from flask import Blueprint, render_template, session, redirect, url_for
from app.db.course_db import get_courses_by_teacher
from app.db.teacher_db import get_teacher_details
from app.db.enrollment_db import get_students_in_course

teacher = Blueprint("teacher", __name__)

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


@teacher.route("/course/<course_id>")
def course_page(course_id):
    if "teacher_username" not in session:
        return redirect(url_for("auth.login_teacher"))

    students = get_students_in_course(course_id)

    return render_template("teacher-course-page.html", 
                           course_id=course_id,
                           students=students)
