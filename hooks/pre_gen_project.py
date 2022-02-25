import re


def get_name():
    return "{{cookiecutter.entity_name}}"


def validate_name():
    name = get_name()

    validation = re.search("^[a-z][a-z]*$", name)

    if(validation == None):
        raise ValueError(
            "The Entiry Name Format is Incorrect --> Only lowercases letters are allowed")


validate_name()
