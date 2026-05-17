from fastapi import FastAPI
from pydantic import BaseModel

from detector import (
    detect_python_errors,
    detect_cpp_errors,
    detect_java_errors
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeRequest(BaseModel):
    code: str
    language: str


@app.get("/")
def home():

    return {
        "message": "AI Syntax Error Detector API Running"
    }


@app.post("/analyze")
def analyze_code(request: CodeRequest):

    language = request.language.lower()

    if language == "python":

        result = detect_python_errors(request.code)

    elif language == "cpp":

        result = detect_cpp_errors(request.code)

    elif language == "java":

        result = detect_java_errors(request.code)

    else:

        result = [{
            "type": "Info",
            "message": f"{request.language} support coming soon.",
            "line": None
        }]

    return {
        "success": True,
        "errors": result
    }
