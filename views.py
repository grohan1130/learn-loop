from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from write_to_mdb import add_student, add_teacher, add_course

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name = "Rohan Gupta")

@views.route("/register-student", methods = ["GET", "POST"])
def register_student():
    if request.method == "POST": # form submitted -> POST request
        #extract form data
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        university = request.form.get("university")
        
        # validate data: checking for missing values
        if not (first_name and last_name and email and username and password and university):
            print("All fields are required!", "error")
            return redirect(url_for("views.register_student"))
        
        # encode form data as a python dictionary (passable to MongoDB)
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

@views.route("/register-teacher", methods = ["GET", "POST"])
def register_teacher():
    if request.method == "POST": # form submitted -> POST request
        #extract form data
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        university = request.form.get("university")
        # Validate and process the data
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

@views.route("/register-course", methods = ["GET", "POST"])
def register_course():
    if request.method == "POST": # form submitted -> POST request
        # extract form data
        department = request.form.get("course-department")
        number = request.form.get("course-number")
        name = request.form.get("course-name")
        # validate and process data
        if not (department and number and name):
            print("All fields are required!", "error")
            return redirect(url_for("views.register_course"))
        course_data = {
            "course_department": department,
            "course_number": number,
            "course_name": name,
        }
        add_course(course_data)
    return render_template("register-course.html")