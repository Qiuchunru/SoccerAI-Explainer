from fastapi import FastAPI
from pydantic import BaseModel

from ai import analyze_match


app = FastAPI()


class MatchRequest(BaseModel):

    description: str



@app.get("/")
def home():

    return {
        "message":
        "Soccer AI Explainer API"
    }



@app.post("/analyze")
def analyze(request: MatchRequest):

    result = analyze_match(
        request.description
    )


    return {

        "analysis": result

    }
