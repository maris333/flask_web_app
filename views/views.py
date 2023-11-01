from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models import Todos
from schemas import TodosSchema

views = Blueprint("views", __name__)
todos_schema = TodosSchema(many=True)

@views.route("/")
def index():
    todos = Todos.query.all()
    todos_json = todos_schema.dump(todos)
    return render_template("index.html", todos=todos_json)

@views.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]
    new_todo = Todos(todo=todo, done=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("views.index"))

@views.route("edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    todo = Todos.query.get(id)
    if request.method == "POST":
        todo.todo = request.form["todo"]
        db.session.commit()
        return redirect(url_for("views.index"))
    else:
        return render_template("edit.html", todo=todo)

@views.route("check/<int:id>")
def check(id):
    todo = Todos.query.get(id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("views.index"))

@views.route("delete/<int:id>")
def delete(id):
    todo = Todos.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("views.index"))
