from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Register routes
    @app.route('/')
    def home():
        return "Welcome to Factory Management System!"
    
    with app.app_context():
        db.create_all()
        
    return app
