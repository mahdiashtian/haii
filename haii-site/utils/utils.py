import os
import ast

TEAM_IMAGE_ROOT = 'haii/'


def get_file_name(file_name):
    base_name = os.path.basename(file_name)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance=None, filename=None):
    name, ext = get_file_name(filename)
    final_name = f"{instance.name}{ext}"
    return f"{TEAM_IMAGE_ROOT}{instance.name}/{final_name}"


def to_dict(value):
    new_value = {}
    for i,x in value.items():
        if isinstance(x,str):
            x = ast.literal_eval(x)
            to_dict(x)
        new_value[i]=x
    return new_value