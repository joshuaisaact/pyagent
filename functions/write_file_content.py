import os
from google.genai import types

def write_file(working_directory, file_path, content):
	abs_working_dir = os.path.abspath(working_directory)
	target_path = os.path.abspath(os.path.join(working_directory, file_path))

	if not target_path.startswith(abs_working_dir + os.sep):
			return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

	try:
		parent_dir = os.path.dirname(target_path)
		os.makedirs(parent_dir, exist_ok=True)
	except Exception as e:
		return f"Error: {e}"

	with open(target_path, "w") as f:
			try:
				f.write(content)
			except Exception as e:
				return f"Error: {e}"


	return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file in the specified working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
				description="The working directory where the file will be written.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)