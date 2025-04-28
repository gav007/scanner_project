# backend/app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scanner import scan_network

app = FastAPI()

# Allow frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scan")
def scan():
    results = scan_network("192.168.0.1/24")
    return {"hosts": results}
