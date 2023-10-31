from flask import Blueprint, render_template, request, redirect, url_for
from src import db
from src.models import Todos
from src.schemas import TodosSchema

read_blueprint = Blueprint("index", __name__)
create_blueprint = Blueprint("add", __name__)
edit_blueprint = Blueprint("edit", __name__)
check_blueprint = Blueprint("check", __name__)
delete_blueprint = Blueprint("delete", __name__)
todos_schema = TodosSchema(many=True)

@read_blueprint.route("/")
def index():
    todos = Todos.query.all()
    todos_json = todos_schema.dump(todos)
    return render_template("index.html", todos=todos_json)

@create_blueprint.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]
    new_todo = Todos(todo=todo, done=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index.index"))

@edit_blueprint.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    todo = Todos.query.get(id)
    if request.method == "POST":
        todo.todo = request.form["todo"]
        db.session.commit()
        return redirect(url_for("index.index"))
    else:
        return render_template("edit.html", todo=todo)

@check_blueprint.route("/check/<int:id>")
def check(id):
    todo = Todos.query.get(id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("index.index"))

@delete_blueprint.route("/delete/<int:id>")
def delete(id):
    todo = Todos.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index.index"))
