from http import HTTPStatus
from fastapi import FastAPI, UploadFile
from AD2PHelper import get_file_name, valid_files
from AD2P import main as AD2PMain

app = FastAPI()

@app.get("/")
async def root():
    return {"AD2P Root"}

@app.get("/Health")
async def health():
    return HTTPStatus.OK

@app.get("/ValidFiles")
async def get_valid_files():
    return {
        "valid_files": valid_files
    }

def write_file_to_scanned_files(file: UploadFile, file_path: str):
    with open(file_path, "wb+") as file_object:
            file_object.write(file.file.read())

@app.post("/AD2PScan")
async def ad2p_scan(file: UploadFile):
    file_path = f"scanned_files/{file.filename}"
    write_file_to_scanned_files(file, file_path)
    scan_result = AD2PMain(file_path)
    
    return {
        "filename": file.filename,
        "scan_result": scan_result
    }


# Request Body should be in the format
# {
#     filename: "filename.extenstion",
#     file_content: "File content"
# }
@app.post("/AD2PScanGodot")
async def ad2p_scan_godot(req_body):
    print(req_body)
    filename = get_file_name(req_body.filename)
    file_path = f"scanned_files/{filename}"
    scan_file = open(file_path, "wb+")
    scan_file.write(req_body.file_content)
    scan_file.close()
    scan_result = AD2PMain(file_path)

    return {
        "filename": file_path,
        "scan_result": scan_result
    }
