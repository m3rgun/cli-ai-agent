import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(target_file):
            dir_name = os.path.dirname(target_file)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name, exist_ok=True)
        with open(target_file, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {str(e)}'
  


if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath("calculator/lorem.txt")))
