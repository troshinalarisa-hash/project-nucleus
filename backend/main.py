from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Backend is running with FastAPI!"}