import ast


def detect_python_errors(code: str):
    errors = []

    try:
        ast.parse(code)
    except SyntaxError as e:
        errors.append({
            "type": "Syntax Error",
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
