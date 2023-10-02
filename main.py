from fastapi import FastAPI, HTTPException, status
import csv

app = FastAPI()
"""
    ## Lista para almacenar los contactos en memoria
"""
contactos = []

"""

    Ruta al archivo CSV
"""
archivo_csv = "contactos.csv"

""" 
    Función para cargar los contactos desde el archivo CSV al iniciar la aplicación
"""
def cargar_contactos():
    try:
        with open(archivo_csv, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contactos.append({"nombre": row["nombre"], "email": row["email"]})
    except FileNotFoundError:
        pass  
        """ Si el archivo no existe, 
            simplemente continua
            con una lista vacía
        """
cargar_contactos()
"""
    Cargamos los contactos desde 
    el archivo CSV al iniciar la aplicación
"""
@app.get("/", status_code=status.HTTP_200_OK, summary="EndPoint raíz")
async def EndPoitn_raíz():
    """
    # EndPoitn raíz
    ## Status codes
    * 289 - Código de muestra
    * 304 - Otor status de prueba
    """
    return {"message": "Hello Niños"}

@app.get("/v1/contactos")
async def listar_contactos():
    """
        # Listar todos los contactos en formato JSON correspondiente
    """
    return {"contactos": contactos}

@app.post("/v1/contactos", status_code=status.HTTP_201_CREATED)
async def crear_contacto(nombre: str, email: str):
    """
        # Crear un nuevo contacto manualmente y guardarlo en el archivo CSV.
    """
    nuevo_contacto = {"nombre": nombre, "email": email}
    contactos.append(nuevo_contacto)

    """ 
        ## Aquí guardar el nuevo contacto en contactos.csv 
    """
    guardar_contacto(nuevo_contacto)

    return {"message": "Contacto creado exitosamente"}

def guardar_contacto(contacto):
    """
    Guardar un contacto en el archivo CSV.
    """
    try:
        """ 
            Abre el archivo CSV en modo escritura 
            (a+ para crear si no existe).
        """
        with open(archivo_csv, mode="a+", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["nombre", "email"]  
            """ 
                Los nombres de las columnas del CSV
            """
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            """ 
                Si el archivo se encuentra vacío se puede escribir los nombres de las columnas
            """
            if csvfile.tell() == 0:
                writer.writeheader()

            """
                Aquí se escribe el nuevo contacto en el CSV
            """
            writer.writerow(contacto)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el contacto en el archivo CSV")