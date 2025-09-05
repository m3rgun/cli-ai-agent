import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):

    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)

    if absolute_path.startswith(os.path.abspath(working_directory)):
        if os.path.isdir(absolute_path):
            try:
                contents = os.listdir(absolute_path)
                files_info = []
                for item in contents:
                    item_path = os.path.join(absolute_path, item)
                    files_info.append(f'- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}')
                return "\n".join(files_info)
            except Exception as e:
                return f'Error listing files: {str(e)}'
        else:
            return f'Error: "{directory}" is not a directory'
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
