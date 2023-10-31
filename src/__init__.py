from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
ma = Marshmallow(app)
ma.init_app(app=app)
db = SQLAlchemy()
db.init_app(app)


#todos = [{"todo": "sample todo", "done": False}]


def create_db():
    with app.app_context():
        db.create_all()


def main():
    from views import views

    app.register_blueprint(views, url_prefix="/")
    create_db()


if __name__ == "__main__":
    main()
    app.run(debug=True, port=5000)
