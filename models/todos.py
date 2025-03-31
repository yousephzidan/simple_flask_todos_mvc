from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Todo(db.Model):
    __tablename__ = "todo"

    id: int = db.Column(db.Integer,primary_key=True)
    title: str = db.Column(db.String)
    description: str = db.Column(db.String)


    def __repr__(self):
        return f"""
Todo 

id: {self.id} 

title: {self.title}

description: {self.description}

"""
