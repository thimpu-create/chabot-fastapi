# main.py

from fastapi import FastAPI
from app import launch_gradio
import threading

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI backend is running"}

# Launch Gradio in a separate thread when FastAPI starts
@app.on_event("startup")
def start_gradio():
    thread = threading.Thread(target=launch_gradio)
    thread.daemon = True
    thread.start()
