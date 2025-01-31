from flask import Flask
from app.routes.auth import auth
from app.routes.teacher import teacher
from app.routes.student import student
from app.routes.main import main

def create_app():
    """Initialize and configure the Flask application."""
    app = Flask(__name__)
    app.secret_key = "your_secret_key"

    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(teacher, url_prefix="/teacher")
    app.register_blueprint(student, url_prefix="/student")

    return app
