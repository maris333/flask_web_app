from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from src.config import Config

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    from src.views import read_blueprint, create_blueprint, edit_blueprint, delete_blueprint, check_blueprint

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(read_blueprint)
    app.register_blueprint(create_blueprint)
    app.register_blueprint(edit_blueprint)
    app.register_blueprint(check_blueprint)
    app.register_blueprint(delete_blueprint)

    return app

def create_db(app):
    with app.app_context():
        db.create_all()
