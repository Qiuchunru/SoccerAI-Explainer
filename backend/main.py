from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai import analyze_match


app = FastAPI(
    title="Soccer AI Explainer",
    description="AI-powered soccer tactical analysis API",
    version="1.0"
)


# Allow React frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



class MatchRequest(BaseModel):

    description: str



@app.get("/")
def home():

    return {
        "message":
        "Soccer AI Explainer API Running"
    }



@app.post("/analyze")
def analyze(request: MatchRequest):

    result = analyze_match(
        request.description
    )

    return {

        "analysis": result

    }
