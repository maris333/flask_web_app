from flask_marshmallow import fields

from src import ma


class TodosSchema(ma.Schema):
    id = fields.fields.Integer()
    todo = fields.fields.Str()
    done = fields.fields.Bool()
