from __init__ import db


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def __init__(self, content, done=False):
        self.content = content
        self.done = done
