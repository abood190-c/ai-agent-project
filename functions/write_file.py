import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_file_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_file_abs, file_path))

        # Check if the target_file path is outside the permitted working directory
        valid_target_file = os.path.commonpath([working_file_abs, target_file]) == working_file_abs
        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Check if target_file is an existing directory
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Ensure all parent directories exist
        parent_dir = os.path.dirname(target_file)
        os.makedirs(parent_dir, exist_ok=True)

        # Open in write mode and overwrite contents
        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites contents to a specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write to, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The content to write into the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
