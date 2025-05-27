def manipulate_file(filename: str, operation: str):
    try:
        with open(filename, "r") as f:
            content = f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

    if operation == "uppercase":
        new_content = content.upper()
    elif operation == "lowercase":
        new_content = content.lower()
    else:
        return "Unsupported operation. Supported: uppercase, lowercase"

    try:
        with open(filename, "w") as f:
            f.write(new_content)
    except Exception as e:
        return f"Error writing file: {str(e)}"

    return f"File {filename} updated with {operation} operation."

