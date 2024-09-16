from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello, FastAPI!"}
