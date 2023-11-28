import os

def read_code_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    return code

def read_code_from_directory(directory):
    code_dict = {}
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                code = read_code_from_file(file_path)
                code_dict[file_path] = code
    return code_dict