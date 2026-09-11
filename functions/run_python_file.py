import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_file_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_file_abs, file_path))

        # Check if the target_file path is outside the permitted working directory
        valid_target_file = os.path.commonpath([working_file_abs, target_file]) == working_file_abs
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if file exists and is a regular file
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # Check if file name ends with .py
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # Build command
        command = ["python", target_file]
        if args is not None:
            command.extend(args)

        # Run process
        result = subprocess.run(
            command,
            cwd=working_file_abs,
            capture_output=True,
            text=True,
            timeout=30
        )

        output_parts = []
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        # If both stdout and stderr contained no output
        if not result.stdout and not result.stderr:
            output_parts.append("No output produced")
        else:
            if result.stdout:
                output_parts.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                output_parts.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file with optional arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional command-line arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}
