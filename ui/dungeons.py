import requests
import json

# Función para obtener las proficiencias de una clase
def obtener_proficiencias(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)['results']
    else:
        return None

# Lista de opciones de clases y sus nombres correspondientes
opciones = [
    {"nombre": "Barbarian", "clase": "barbarian"},
    {"nombre": "Bard", "clase": "bard"},
    {"nombre": "Cleric", "clase": "cleric"},
    {"nombre": "Druid", "clase": "druid"},
    {"nombre": "Fighter", "clase": "fighter"},
    {"nombre": "Monk", "clase": "monk"},
    {"nombre": "Paladin", "clase": "paladin"},
    {"nombre": "Ranger", "clase": "ranger"},
    {"nombre": "Rogue", "clase": "rogue"},
    {"nombre": "Sorcerer", "clase": "sorcerer"},
    {"nombre": "Warlock", "clase": "warlock"},
    {"nombre": "Wizard", "clase": "wizard"},
]

# Mostrar las opciones al usuario
for i, opcion in enumerate(opciones, start=1):
    print(f"{i}.- {opcion['nombre']}")

# Obtener la opción del usuario
opcion = input("Seleccione una opción (1-12): ")

# Verificar si la opción es válida
if opcion.isdigit() and 1 <= int(opcion) <= len(opciones):
    seleccion = opciones[int(opcion) - 1]
    print(f"Seleccionaste a {seleccion['nombre']}")
    
    # Construir la URL de la API
    URL = f"https://www.dnd5eapi.co/api/classes/{seleccion['clase']}/proficiencies"

    # Obtener las proficiencias de la clase seleccionada
    proficiencias = obtener_proficiencias(URL)

    if proficiencias:
        for x, proficiency in enumerate(proficiencias, start=1):
            print(f"{x}.- {proficiency['name']}")
    else:
        print("Error en la solicitud.")
else:
    print("Opción no válida.")