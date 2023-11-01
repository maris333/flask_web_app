from flask_marshmallow import fields

from app import ma


class TodosSchema(ma.Schema):
    id = fields.fields.Integer()
    todo = fields.fields.Str()
    done = fields.fields.Bool()
