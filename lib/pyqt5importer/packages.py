import json

def find_class_package(class_name, packages_file_path):
    packages_file = open(packages_file_path, 'r')
    packages = json.load(packages_file)

    return packages[class_name] if class_name in packages else False
