import ast
import subprocess
import tempfile
import os


# Python Detection
def detect_python_errors(code: str):

    errors = []

    try:
        ast.parse(code)

    except SyntaxError as e:
        errors.append({
            "type": "Python Syntax Error",
            "message": str(e),
            "line": e.lineno
        })

    if "== True" in code:
        errors.append({
            "type": "Logical Warning",
            "message": "Avoid using '== True'.",
            "line": None
        })

    if "== False" in code:
        errors.append({
            "type": "Logical Warning",
            "message": "Avoid using '== False'.",
            "line": None
        })

    return errors


# C++ Detection
def detect_cpp_errors(code: str):

    import re

    errors = []

    with tempfile.NamedTemporaryFile(delete=False, suffix=".cpp") as temp:

        temp.write(code.encode())

        temp_file = temp.name

    result = subprocess.run(
        ["g++", temp_file],
        capture_output=True,
        text=True
    )

    if result.stderr:

        matches = re.findall(r'error: (.*)', result.stderr)

        if matches:
            formatted_message = "\n".join(matches)

        else:
            formatted_message = result.stderr

        errors.append({
            "type": "C++ Compilation Error",
            "message": formatted_message,
            "line": None
        })

    os.remove(temp_file)

    return errors

# Java Detection
def detect_java_errors(code: str):

    errors = []

    with tempfile.NamedTemporaryFile(delete=False, suffix=".java") as temp:

        temp.write(code.encode())

        temp_file = temp.name

    result = subprocess.run(
        ["javac", temp_file],
        capture_output=True,
        text=True
    )

    if result.stderr:
        errors.append({
            "type": "Java Compilation Error",
            "message": result.stderr,
            "line": None
        })

    os.remove(temp_file)

    return errors
