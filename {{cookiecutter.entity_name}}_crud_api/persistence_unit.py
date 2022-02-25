import json


def get_{{cookiecutter.entity_name}}(id):
    return f"You're trying getting the {{cookiecutter.entity_name}} [Id={id}], a NotImplementedError was raised", 501


def create_{{cookiecutter.entity_name}}(payload):
    data = {
        "message": "You're trying to Create a {{cookiecutter.entity_name}}, a NotImplementedError was raised",
        "payload": payload
    }
    return json.dumps(data), 501


def update_{{cookiecutter.entity_name}}(payload):
    data = {
        "message": "You're trying to Update a {{cookiecutter.entity_name}}, a NotImplementedError was raised",
        "payload": payload
    }
    return json.dumps(data), 501


def delete_{{cookiecutter.entity_name}}(id):
    return f"You're trying to Delete a {{cookiecutter.entity_name}} [Id={id}], a NotImplementedError was raised", 501
