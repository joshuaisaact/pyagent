import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_path.startswith(abs_working_dir + os.sep):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_path):
        return f'Error: File "{file_path}" not found.'

    if not target_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed = subprocess.run(
            ["python3", target_path] + args,
            timeout=30,
            capture_output=True,
            text=True,
            cwd=abs_working_dir
        )

        result = ""
        if completed.stdout:
            result += f"STDOUT:\n{completed.stdout}"

        if completed.stderr:
            if result:
                result += "\n"
            result += f"STDERR:\n{completed.stderr}"

        if completed.returncode != 0:
            if result:
                result += "\n"
            result += f"Process exited with code {completed.returncode}"

        if not result:
            return "No output produced."

        return result

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in the specified working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory where the Python file is located.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Arguments to pass to the Python script.",
            ),
        },
    ),
)