from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from parser import analyze_url

app = FastAPI(title="Page Pulse API")

# Allow frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to Page Pulse API"}

@app.get("/analyze")
def analyze(url: str):
    return analyze_url(url)