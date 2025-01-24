from flask import Blueprint, render_template, request, redirect, url_for, flash

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name = "Rohan Gupta")

@views.route("/register-student", methods = ["GET", "POST"])
def register_student():
    if request.method == "POST":
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
            return redirect(url_for("views.register_student"))
        # Example: Print data (replace with database logic)
        print(f"New student registered: {first_name} {last_name}, Email: {email}, University: {university}")
    return render_template("register-student.html")

@views.route("/register-teacher", methods = ["GET", "POST"])
def register_teacher():
    if request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        university = request.form.get("university")
         # Validate and process the data
        if not (first_name and last_name and email and username and password and university):
            print("All fields are required!", "error")
            return redirect(url_for("views.register_student"))
        # Example: Print data (replace with database logic)
        print(f"New teacher registered: {first_name} {last_name}, Email: {email}, University: {university}")
    return render_template("register-teacher.html")