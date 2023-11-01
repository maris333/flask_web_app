from app import db, app


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, todo, done=False):
        self.todo = todo
        self.done = done


def create_db():
    with app.app_context():
        db.create_all()
