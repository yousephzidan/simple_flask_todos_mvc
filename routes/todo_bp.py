from flask import Blueprint
from controllers.TodoController import index



todo_bp = Blueprint('todos', __name__) 


todo_bp.get("/")(index) 




