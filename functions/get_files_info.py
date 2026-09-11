import os
def get_files_info(working_directory: str, directory: str = ".") -> str:
    """
    Get information about files in the specified directory.

    Args:
        working_directory (str): The working directory to search for files.
        directory (str): The directory to get file information from. Defaults to the current directory.

    Returns:
        str: A string containing information about the files in the specified directory.
    """
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    if not os.path.exists(target_dir):
        return f"Error: Directory '{target_dir}' does not exist."

    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
  
    # If any errors are raised by the standard library functions that you call, catch them and instead return a string describing the error. You may find it convenient to put everything in this function in a try/except block. When returning an error string, always prefix it with Error:.



    #After the path validation succeeds, iterate over the items in the target directory. For each item, record:

    #     The name
    #     The file size
    #     Whether it's a directory

    # Use that data to build and return a string representing the contents of the target directory. It should use this format:

    # - README.md: file_size=1032 bytes, is_dir=False
    # - src: file_size=128 bytes, is_dir=True
    # - package.json: file_size=1234 bytes, is_dir=False



    files_info = []
    for item in os.listdir(target_dir):
        file_path = os.path.join(target_dir, item)
        
        file_size = os.path.getsize(file_path)
        files_info.append(f"{item}: file_size={file_size} bytes, is_dir={os.path.isdir(file_path)}")
        

    if not files_info:
        return f"Error: No files found in directory '{target_dir}'."

    return "\n".join(files_info)

if __name__ == "__main__":
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))
    print(get_files_info("calculator", "main.py"))

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
