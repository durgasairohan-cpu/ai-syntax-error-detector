from fastapi import FastAPI
from pydantic import BaseModel
from detector import detect_python_errors
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
    return {"message": "AI Syntax Error Detector API Running"}


@app.post("/analyze")
def analyze_code(request: CodeRequest):

    if request.language.lower() == "python":
        result = detect_python_errors(request.code)
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
