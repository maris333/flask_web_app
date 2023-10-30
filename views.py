from flask import Blueprint, render_template, request, redirect, url_for

from app import todos

views = Blueprint(__name__, "views")


@views.route("/")
def index():
    return render_template("index.html", todos=todos)


@views.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]
    todos.append({"todo": todo, "done": False})
    return redirect(url_for("views.index"))


@views.route("edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo["todo"] = request.form["todo"]
        return redirect(url_for("views.index"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@views.route("check/<int:index>")
def check(index):
    todos[index]["done"] = not todos[index]["done"]
    return redirect(url_for("index"))


@views.route("delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("views.index"))
