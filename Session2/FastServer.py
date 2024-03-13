from fastapi import FastAPI

app = FastAPI()

@app.get("/Masoud")
async def read_root():
    return {"message": "Hello, World!"}
