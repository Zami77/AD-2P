from fastapi import FastAPI
from AD2PHelper import valid_files

app = FastAPI()


@app.get("/")
async def root():
    return {"AD2P Root"}

@app.get("/ValidFiles")
async def get_valid_files():
    return {
        "valid_files": valid_files
    }
