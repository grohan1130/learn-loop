from flask import Blueprint, render_template, session, redirect, url_for

student = Blueprint("student", __name__)

# Student Dashboard
@student.route("/student-dashboard")
def student_dashboard():
    if "student_username" not in session:
        return redirect(url_for("auth.login_student"))

    return render_template("student-dashboard.html", first_name=session["student_first_name"])
