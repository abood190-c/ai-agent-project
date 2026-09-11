import os
import config
MAX_CHARS = config.max_char
def get_file_content(working_directory: str, file_path: str) -> str:
    working_file_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_file_abs, file_path))


    if not os.path.isfile(target_file) or not os.path.exists(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'


    # Will be True or False
    valid_target_file = os.path.commonpath([working_file_abs, target_file]) == working_file_abs
    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'


    with open(target_file, 'r') as f:
            
        content = f.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    return content