from flask import Blueprint, render_template, request, redirect, url_for, session
from write_to_mdb import add_course

teacher = Blueprint("teacher", __name__)

# Teacher Dashboard
@teacher.route("/teacher-dashboard")
def teacher_dashboard():
    if "teacher_username" not in session:
        return redirect(url_for("auth.login_teacher"))

    return render_template("teacher-dashboard.html", first_name=session["teacher_first_name"])


# Register Course (Only for logged-in teachers)
@teacher.route("/register-course", methods=["GET", "POST"])
def register_course():
    if "teacher_username" not in session:
        return redirect(url_for("auth.login_teacher"))

    if request.method == "POST":
        department = request.form.get("department")
        number = request.form.get("number")
        name = request.form.get("name")

        if not (department and number and name):
            print("All fields are required!", "error")
            return redirect(url_for("teacher.register_course"))

        course_data = {
            "course_department": department,
            "course_number": number,
            "course_name": name,
            "teacher_username": session["teacher_username"]
        }
        add_course(course_data)

        return redirect(url_for("teacher.teacher_dashboard"))

    return render_template("register-course.html", teacher_username=session["teacher_username"])
