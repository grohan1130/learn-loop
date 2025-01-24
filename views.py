from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name = "Rohan Gupta")

@views.route("/register-student")
def register_student():
    return render_template("register-student.html")

@views.route("/register-teacher")
def register_teacher():
    return render_template("register-teacher.html")