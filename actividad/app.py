from fastapi import FastAPI, HTTPException, File, UploadFile, Query
from pydantic import BaseModel
import csv
from PIL import Image, ImageOps
from io import BytesIO
import hashlib
import qrcode
import os

app = FastAPI()

class Contacto(BaseModel):
    id_contacto: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    email: str
    telefono: str

@app.get('/contactos', response_model=list[Contacto])
def get_contactos():
    try:
        with open('contactos.csv', mode='r') as file:
            reader = csv.DictReader(file)
            contactos = [Contacto(**row) for row in reader]

        return contactos
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

image_directory = 'static/imagenes/'

@app.post('/contactos', response_model=Contacto)
def add_contacto(contacto: Contacto):
    try:
        with open('contactos.csv', mode='a', newline='') as file:
            fieldnames = ['id_contacto', 'nombre', 'primer_apellido', 'segundo_apellido', 'email', 'telefono']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(contacto.dict())

        return contacto
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.patch('/contactos/{id}', response_model=Contacto)
def update_contacto(id_contacto: int, contacto: Contacto):
    try:
        with open('contactos.csv', mode='r') as file:
            reader = csv.DictReader(file)
            contactos = [row for row in reader]

        updated_contactos = []
        contacto_updated = False

        for c in contactos:
            if int(c['id_contacto']) == id_contacto:
                c.update(contacto.dict())
                contacto_updated = True
            updated_contactos.append(c)

        if not contacto_updated:
            raise HTTPException(status_code=404, detail="Contacto no encontrado")

        with open('contactos.csv', mode='w', newline='') as file:
            fieldnames = ['id_contacto', 'nombre', 'primer_apellido', 'segundo_apellido', 'email', 'telefono']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_contactos)

        return contacto
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 1.5 Programar el endpoint DELETE /contactos/{id_contacto}
@app.delete('/contactos/{id}', response_model=dict)
def delete_contacto(id_contacto: int):
    try:
        with open('contactos.csv', mode='r') as file:
            reader = csv.DictReader(file)
            contactos = [row for row in reader]

        contacto_deleted = False

        updated_contactos = [c for c in contactos if int(c['id_contacto']) != id_contacto]

        if len(contactos) == len(updated_contactos):
            raise HTTPException(status_code=404, detail="Contacto no encontrado")

        with open('contactos.csv', mode='w', newline='') as file:
            fieldnames = ['id_contacto', 'nombre', 'primer_apellido', 'segundo_apellido', 'email', 'telefono']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_contactos)

        return {"message": "Contacto eliminado exitosamente"}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 1.6 Programar el endpoint GET /contactos/buscar
@app.get('/contactos/buscar', response_model=list[Contacto])
def search_contactos(nombre: str = Query(..., title="Nombre a buscar")):
    try:
        with open('contactos.csv', mode='r') as file:
            reader = csv.DictReader(file)
            contactos = [row for row in reader if nombre.lower() in row['nombre'].lower()]

        if len(contactos) > 0:
            return contactos
        else:
            raise HTTPException(status_code=404, detail="No se encontraron contactos con ese nombre")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/imagenes', response_model=dict)
def upload_image(image: UploadFile):
    try:
        image_data = Image.open(image.file)
        image_data.save(image_directory + image.filename)
        return {"message": "Imagen guardada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/imagenes/efectos', response_model=dict)
def apply_image_effects(image: UploadFile, crop: str = Query(None), fliph: bool = Query(False), colorize: bool = Query(False)):
    try:
        image_data = Image.open(image.file)

        if crop:
            left, top, right, bottom = map(int, crop.split(','))
            image_data = image_data.crop((left, top, right, bottom))

        if fliph:
            image_data = image_data.transpose(Image.FLIP_LEFT_RIGHT)

        if colorize:
            image_data = ImageOps.colorize(image_data, 'red', 'yellow')

        image_data.save(image_directory + 'modified_' + image.filename)
        return {"message": "Efectos aplicados exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
qr_directory = 'static/qrcodes/'

@app.get('/generar_codigo_qr')
def generar_codigo_qr(texto: str):
    try:
        img = qrcode.make(texto)
        file_name = f"qr_{texto[0]}.png"
        file_path = os.path.join(qr_directory, file_name)
        img.save(file_path)  
        return {"message": f"Código QR generado exitosamente y guardado en {file_path}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)