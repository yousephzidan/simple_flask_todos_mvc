from flask import Flask
from routes.todo_bp import todo_bp


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    
    # App configuration 
    app.config.from_object("config.Development")

    # Registering Blueprints
    app.register_blueprint(todo_bp)

    return app

if "__main__" == __name__:
    app = create_app()
    app.run()

