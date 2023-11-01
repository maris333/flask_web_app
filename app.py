from flask import Flask, redirect, url_for, render_template, request
from flask_marshmallow import Marshmallow, fields
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)


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


class TodosSchema(ma.Schema):
    id = fields.fields.Integer()
    todo = fields.fields.Str()
    done = fields.fields.Bool()


todos_schema = TodosSchema(many=True)


@app.route("/")
def index():
    todos = Todos.query.all()
    todos_json = todos_schema.dump(todos)
    return render_template("index.html", todos=todos_json)


@app.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]
    new_todo = Todos(todo=todo, done=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    todo = Todos.query.get(id)
    if request.method == "POST":
        todo.todo = request.form["todo"]
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo)


@app.route("/check/<int:id>")
def check(id):
    todo = Todos.query.get(id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:id>")
def delete(id):
    todo = Todos.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":

    create_db()

    app.run(debug=True, port=5000)
