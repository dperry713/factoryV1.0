from flask import Flask
from app.extensions import db, migrate
from app.blueprints import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    register_blueprints(app)
    
    return app
