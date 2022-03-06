from fastapi import FastAPI, UploadFile
from AD2PHelper import valid_files
from AD2P import main

app = FastAPI()

@app.get("/")
async def root():
    return {"AD2P Root"}

@app.get("/ValidFiles")
async def get_valid_files():
    return {
        "valid_files": valid_files
    }

@app.post("/AD2PScan")
async def ad2p_scan(file: UploadFile):
    # TODO: have to save file locally and send that path to AD2P
    return {
        "filename": file.filename,
        "scan_result": main(file.filename)
    }
