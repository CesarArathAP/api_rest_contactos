import os
from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Monta el directorio "static" para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    saved_file_paths = []
    for i, file in enumerate(files):
        file_path = os.path.join("static", "imagenes", f"file_{i}.bin")
        with open(file_path, "wb") as f:
            f.write(file)
        saved_file_paths.append(file_path)
    return {"saved_file_paths": saved_file_paths}

@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    saved_file_paths = []
    for i, file in enumerate(files):
        file_path = os.path.join("static", "pdf", file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        saved_file_paths.append(file_path)
    return {"saved_file_paths": saved_file_paths}

@app.get("/")
async def main():
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)