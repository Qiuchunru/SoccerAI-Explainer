from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from prompts import build_prompt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Soccer AI Explainer running"}

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    text = data.get("text", "")

    prompt = build_prompt(text)

    # ===== 模拟 IBM Granite（你之后替换这里）=====
    ai_response = f"[MOCK AI RESPONSE]\n\n{prompt}"

    return JSONResponse({
        "input": text,
        "analysis": ai_response
    })
