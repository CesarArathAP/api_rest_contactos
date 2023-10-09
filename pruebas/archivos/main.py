import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import List

app = FastAPI()

# Monta el directorio "static" para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/files/")
async def create_files(files: List[UploadFile] = File(...)):
    saved_file_paths = []
    for i, file in enumerate(files):
        file_path = os.path.join("static", "imagenes", f"{file.filename}")
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        saved_file_paths.append(file_path)
    return {"saved_file_paths": saved_file_paths}

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    saved_file_paths = []
    for i, file in enumerate(files):
        file_path = os.path.join("static", "pdf", f"{file.filename}")
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        saved_file_paths.append(file_path)
    return {"saved_file_paths": saved_file_paths}

@app.get("/")
async def main():
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input type="file" name="files" multiple>
    <input type="submit" value="Subir archivos">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input type="file" name="files" multiple>
    <input type="submit" value="Subir archivos PDF">
    </form>
    </body>
    """
    return HTMLResponse(content=content)