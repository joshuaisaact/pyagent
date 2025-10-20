import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not (target_path == abs_working_dir or target_path.startswith(abs_working_dir + os.sep)):
          return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_path):
          return f'Error: File not found or is not a regular file: "{file_path}"'



    try:
        with open(target_path, "r") as f:
            file_length = len(f.read())
            f.seek(0)
            file_content_string = f.read(MAX_CHARS)
            if file_length > MAX_CHARS:
                return file_content_string + f"[...File '{file_path} truncated at {MAX_CHARS} characters]"
            else:
                return file_content_string
    except Exception as e:
         return f"Error reading file: {e}"

