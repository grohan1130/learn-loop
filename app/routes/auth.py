from flask import Blueprint, render_template, request, redirect, url_for, session
from app.db.student_db import add_student, verify_login_student
from app.db.teacher_db import add_teacher, verify_login_teacher

auth = Blueprint("auth", __name__)

@auth.route("/register-student", methods=["GET", "POST"])
def register_student():
    if request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        university = request.form.get("university")

        if not (first_name and last_name and email and username and password and university):
            return redirect(url_for("auth.register_student"))

        student_data = {
            "student_first_name": first_name,
            "student_last_name": last_name,
            "student_email": email,
            "student_username": username,
            "student_password": password,
            "student_university": university
        }
        add_student(student_data)
        return redirect(url_for("auth.login_student"))

    return render_template("register-student.html")


@auth.route("/register-teacher", methods=["GET", "POST"])
def register_teacher():
    if request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        university = request.form.get("university")

        if not (first_name and last_name and email and username and password and university):
            return redirect(url_for("auth.register_teacher"))

        teacher_data = {
            "teacher_first_name": first_name,
            "teacher_last_name": last_name,
            "teacher_email": email,
            "teacher_username": username,
            "teacher_password": password,
            "teacher_university": university
        }
        add_teacher(teacher_data)
        return redirect(url_for("auth.login_teacher"))

    return render_template("register-teacher.html")


@auth.route("/login-student", methods=["GET", "POST"])
def login_student():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        student = verify_login_student({"student_username": username, "student_password": password})

        if student:
            session["student_username"] = student["student_username"]
            session["student_first_name"] = student["student_first_name"]
            return redirect(url_for("student.student_dashboard"))

    return render_template("login-student.html")


@auth.route("/login-teacher", methods=["GET", "POST"])
def login_teacher():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        teacher = verify_login_teacher({"teacher_username": username, "teacher_password": password})

        if teacher:
            session["teacher_username"] = teacher["teacher_username"]
            session["teacher_first_name"] = teacher["teacher_first_name"]
            return redirect(url_for("teacher.teacher_dashboard"))

    return render_template("login-teacher.html")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login_student"))
