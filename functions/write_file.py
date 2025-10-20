import os

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
