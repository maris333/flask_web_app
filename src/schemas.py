from flask_marshmallow import fields
from __init__ import ma


class TodosSchema(ma.Schema):
    id = fields.fields.Integer()
    content = fields.fields.Str()
    done = fields.fields.Bool()
