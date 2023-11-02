from src import db


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, todo, done=False):
        self.todo = todo
        self.done = done
