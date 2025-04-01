from flask import url_for
from flask import request
from flask import redirect 
from models.todos import db 
from models.todos import Todo
from flask import render_template



def index():
    todos = Todo.query.all()
    return render_template("index.html",todos=todos)

def update_todo():
    """Update Todo"""
    id, title, description = request.form

    print(title,description)
    return redirect(url_for("index"))


def add_todo():
    """Add Todo"""
    title, description   = request.form

    print(title,description)
    return redirect(url_for("index"))

def delete_todo(todo_id):
    """Delete Todo"""
    Todo.query.filter_by(id=todo_id).delete()
    db.session.commit()

    return redirect(url_for("index"))






