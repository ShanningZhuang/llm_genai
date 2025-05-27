import os, glob

# Function specifications for API function calling
tools = [
  {
    "type": "function",
    "function": {
      "name": "read_file",
      "description": "Read the content of a local file",
      "parameters": {
        "type": "object",
        "properties": {
          "path": {"type": "string", "description": "The file path to read"}
        },
        "required": ["path"],
        "additionalProperties": False
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "write_file",
      "description": "Write content to a local file",
      "parameters": {
        "type": "object",
        "properties": {
          "path": {"type": "string", "description": "The file path to write to"},
          "content": {"type": "string", "description": "The content to write"}
        },
        "required": ["path", "content"],
        "additionalProperties": False
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "delete_file",
      "description": "Delete a local file",
      "parameters": {
        "type": "object",
        "properties": {
          "path": {"type": "string", "description": "The file path to delete"}
        },
        "required": ["path"],
        "additionalProperties": False
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "list_directory",
      "description": "List files in a directory with optional glob pattern",
      "parameters": {
        "type": "object",
        "properties": {
          "path": {"type": "string", "description": "Directory path to list"},
          "pattern": {"type": "string", "description": "Optional glob pattern, e.g. '*.txt'"}
        },
        "required": ["path"],
        "additionalProperties": False
      }
    }
  }
]

# Implementations

def read_file(path: str) -> str:
    if not os.path.isfile(path):
        return f"Error: '{path}' not found."
    return open(path, 'r', encoding='utf-8').read()


def write_file(path: str, content: str) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"Wrote '{path}'"


def delete_file(path: str) -> str:
    try:
        os.remove(path)
        return f"Deleted '{path}'"
    except FileNotFoundError:
        return f"Error: '{path}' not found."


def list_directory(path: str, pattern: str = '*') -> list:
    if not os.path.isdir(path):
        return f"Error: '{path}' not found or not a directory."
    return glob.glob(os.path.join(path, pattern))
