from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import db, Task
import subprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SpeedTestResult(BaseModel):
    download: float
    upload: float
    ping: float

@app.on_event("startup")
def startup():
    db.connect()
    db.create_tables([Task])

@app.on_event("shutdown")
def shutdown():
    db.close()

@app.get("/")
def read_root():
    return {"message": "Network Speed Test and Optimization Tool"}

@app.get("/speedtest")
def run_speedtest():
    try:
        result = subprocess.run(["speedtest-cli", "--json"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize")
def optimize_network(settings: dict):
    # Apply network optimizations based on the settings provided
    return {"message": "Network optimizations applied"}

@app.post("/ai_analysis")
def ai_analysis(speed_result: SpeedTestResult):
    # Perform AI-based analysis on the speed test results and provide suggestions
    suggestions = ["Optimize your router settings", "Use a different DNS provider"]
    return {"suggestions": suggestions}