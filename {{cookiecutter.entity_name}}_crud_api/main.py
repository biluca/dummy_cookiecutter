import json
import time
from flask import *
import persistence_unit as pu

app = Flask(__name__)
API_ROOT = '/api/v1'


def resource_name():
    return f"{API_ROOT}/{{cookiecutter.entity_name}}"


@app.route(API_ROOT, methods=['GET'])
def home():
    return render_template('/index.html')


@app.route(f"{resource_name()}/<id>", methods=['GET'])
def get_{{cookiecutter.entity_name}}(id):
    return pu.get_{{cookiecutter.entity_name}}(id)


@app.route(resource_name(), methods=['POST'])
def create_{{cookiecutter.entity_name}}():
    payload = request.json
    return pu.create_{{cookiecutter.entity_name}}(payload)


@app.route(resource_name(), methods=['PUT'])
def update_{{cookiecutter.entity_name}}():
    payload = request.json
    return pu.update_{{cookiecutter.entity_name}}(payload)


@app.route(f"{resource_name()}/<id>", methods=['DELETE'])
def delete_{{cookiecutter.entity_name}}(id):
    return pu.delete_{{cookiecutter.entity_name}}(id)


if __name__ == '__main__':
    app.run(port=8080)
