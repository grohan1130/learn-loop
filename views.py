from flask import Blueprint, render_template, request, redirect, url_for, session
from write_to_mdb import (
    add_student, add_teacher, add_course,
    verify_login_teacher, verify_login_student
)

views = Blueprint(__name__, "views")

# Home Page
@views.route("/")
def home():
    return render_template("index.html", name="Rohan Gupta")


# Student Registration
@views.route("/register-student", methods=["GET", "POST"])
def register_student():
    if request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        university = request.form.get("university")

        if not (first_name and last_name and email and username and password and university):
            print("All fields are required!", "error")
            return redirect(url_for("views.register_student"))

        student_data = {
            "student_first_name": first_name,
            "student_last_name": last_name,
            "student_email": email,
            "student_username": username,
            "student_password": password,
            "student_university": university
        }
        add_student(student_data)

    return render_template("register-student.html")


# Teacher Registration
@views.route("/register-teacher", methods=["GET", "POST"])
def register_teacher():
    if request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        university = request.form.get("university")

        if not (first_name and last_name and email and username and password and university):
            print("All fields are required!", "error")
            return redirect(url_for("views.register_teacher"))

        teacher_data = {
            "teacher_first_name": first_name,
            "teacher_last_name": last_name,
            "teacher_email": email,
            "teacher_username": username,
            "teacher_password": password,
            "teacher_university": university
        }
        add_teacher(teacher_data)

    return render_template("register-teacher.html")


# Student Login
@views.route("/login-student", methods=["GET", "POST"])
def login_student():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not (username and password):
            print("All fields are required!", "error")
            return redirect(url_for("views.login_student"))

        student = verify_login_student({"student_username": username, "student_password": password})

        if student:
            session["student_username"] = student["student_username"]
            session["student_first_name"] = student["student_first_name"]
            return redirect(url_for("views.student_dashboard"))
        else:
            print("Invalid credentials!", "error")
            return redirect(url_for("views.login_student"))

    return render_template("login-student.html")


# Teacher Login
@views.route("/login-teacher", methods=["GET", "POST"])
def login_teacher():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not (username and password):
            print("All fields are required!", "error")
            return redirect(url_for("views.login_teacher"))

        teacher = verify_login_teacher({"teacher_username": username, "teacher_password": password})

        if teacher:
            session["teacher_username"] = teacher["teacher_username"]
            session["teacher_first_name"] = teacher["teacher_first_name"]
            return redirect(url_for("views.teacher_dashboard"))
        else:
            print("Invalid credentials!", "error")
            return redirect(url_for("views.login_teacher"))

    return render_template("login-teacher.html")


# Dashboards
@views.route("/teacher-dashboard")
def teacher_dashboard():
    if "teacher_username" not in session:
        return redirect(url_for("views.login_teacher"))
    return render_template("teacher-dashboard.html", first_name=session["teacher_first_name"])

@views.route("/student-dashboard")
def student_dashboard():
    if "student_username" not in session:
        return redirect(url_for("views.login_student"))
    return render_template("student-dashboard.html", first_name=session["student_first_name"])


# Logout (Handles Both Students & Teachers)
@views.route("/logout")
def logout():
    session.clear()  # Clears all session data
    return redirect(url_for("views.home"))
