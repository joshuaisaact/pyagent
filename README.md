## PyAgent - AI Code Assistant

A simple AI-powered code agent that can interact with your filesystem and execute Python code using Google's Gemini API.

### Features

- File Operations: List, read, and write files in a working directory
- Code Execution: Run Python scripts with arguments
- Agentic Loop: Iteratively calls functions up to 20 times to complete complex tasks
- Safety: Restricts all operations to a designated working directory

### Setup

1. Install dependencies:

```
uv sync
```

2. Create a .env file with a Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### Usage

```
uv run main.py "your prompt here"
```

### Examples

```
# Read a file
uv run main.py "get the contents of lorem.txt"

# Run tests
uv run main.py "run tests.py"

# Create a file
uv run main.py "create a README.md file with the contents '# My Project'"

# Analyze code
uv run main.py "how does the calculator render results to the console?"

# Enable verbose mode for debugging
uv run main.py "list all files" --verbose
```

### Available Functions

- `get_files_info(path)` - List files and directories
- `get_file_content(file_path)` - Read file contents
- `run_python_file(file_path, args)` - Execute Python scripts
- `write_file(file_path, content)` - Create or overwrite files

### Safety Notes

⚠️ **This is a learning project, not production-ready!**

- The agent can execute arbitrary Python code
- Operations are restricted to the working directory
- Python execution has a 30-second timeout
- Maximum 20 agent iterations per request

**Do not share this with others for general use** - it lacks the security features needed for production.