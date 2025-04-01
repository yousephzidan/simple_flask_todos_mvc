from flask import Flask
from routes.todo_bp import todo_bp
from models.todos import db

def create_app() -> Flask:
    """Create Flask and configuring it"""
    app: Flask = Flask(__name__)
    
    # App configuration 
    app.config.from_object("config.Development")

    # Registering Blueprints
    app.register_blueprint(todo_bp)

    # Initializing our SQL database 
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

if "__main__" == __name__:
    app = create_app()
    app.run()

