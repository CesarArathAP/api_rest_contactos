from fastapi import FastAPI
import csv

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Niños"}

@app.get("/v1/contactos")
async def contactos():
    contactos = []

    try:
        with open("contactos.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contactos.append({"nombre": row["nombre"], "email": row["email"]})
    except FileNotFoundError:
        return {"error": "No conozco ese archivo padrino DX"}

    response = { "contactos": contactos}
    return response