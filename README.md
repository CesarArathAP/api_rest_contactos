# Desing Document: API REST CONTACTOS

## 1. Descripción
Ejemplo de una API REST para gestionar contactos en una DB utilizando FastAPI.

## 2. Objetivo
Realizar un ejemplo de diseño de una API REST de tipo CRUD y su posterior codificación utilizando el framework [FastAPI](https://fastapi.tiangolo.com/).

## 3. Diseño de la BD
Para este ejemplo se utilizará el gestor de base de datos [SQLite3](https://sqlite.org) con las siguientes tablas:

### 3.1 Tabla: contactos
|No,|Campo|Tipo|Resticciones|Descripción|
|--|--|--|--|--|
|1|id_contactos|int|PRIMARY KEY|Llave primaria de la tabla|
|2|nombre|varchar|100|Tipo texto|
|3|primer_apellido|varchar|50|Tipo Texto|
|4|segundo_apellido|varchar|50|Tipo texto|
|5|email|varchar|50|Tipo Texto|
|6|telefono|varchar|13|Tipo Texto|

## 3.2 Script

```sql
CREATE TABLE contactos (
    id_contacto INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    primer_apellido VARCHAR(50) NOT NULL,
    segundo_apellido VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    telefono VARCHAR(13) NOT NULL
);
```
## 4. Desing Document

## 4.1 Metodo PUT

|Propiedad|Detalle|
|--|--|
|Descripción|EndPoint para actualizar algun contacto de la API|
|Summary|EndPoint para actualizar datos de los contactos|
|Metodo|PUT|
|EndPoint|https://localhost:8000/contactos/{id}|
|Query Param|NA|
|Path Param|'id''int'|
|Data|{"id_contacto","123", "nombre":"Dejahn", "primer_apellido":"Lopez", "segundo_apellido":"Perez", "email":"dejahn@gmail.com", "telefono":"123456789"}|
|Versión|V1|
|Status Code|200 OK|
|Response Type|application/json|
|Response|{"version":"v1", "mensaje":"contacto_actualizado", "datatime": "25/09/23 17:16:15"}|
|Curl|curl -X PUT https://localhost:8000/contacto/{id} -H accept:application/json -d {data: Jonth}|
|Status Code (error)|400 Bad Raquest|
|Response Type(error)|JSON|
|Response (error)|{"error":"Dato Invalido"}|

## 4.2 Metodo PATCH

|Propiedad|Detalle|
|--|--|
|Descripción|EndPoint para realizar modificaciones parciales en un contacto|
|Summary|EndPoint para modificar datos de un contacto de forma parcial|
|Metodo|PATCH|
|EndPoint|https://localhost:8000/contactos/{id}|
|Query Param|NA|
|Path Param|{id} int|
|Data|{"id_contacto","123", "email:"dejahn@gmail.com", "telefono":"987654321"}|
|Versión|V1|
|Status Code|200 OK|
|Response Type|json|
|Response|{"response":"V1" PATCH:"contactos"datatime":"25/09/23 17:16:15"}|
|Curl|curl -X PATCH https://localhost:8000/contactos/123 -d {"email":"modificacion@gmail.com"}|
|Status Code (error)|400 Bad Raquest|
|Response Type(error)|application/json|
|Response (error)|{"error":"Changes could not be applied"}|

## 4.3 Metodo POST

|Propiedad|Detalle|
|--|--|
|Descripción|EndPoint para crear un nuevo contacto|
|Summary|EndPoint para crear un contacto con los datos proporcionados|
|Metodo|POST|
|EndPoint|https://localhost:8000/|
|Query Param|NA|
|Path Param|{"id_contacto":"126", "nombre":"Dejohn", "primer_apellido": "Lopéz", "segundo_apellido":"Snchez", "email":"dejohn@gmail.com", "telefono":"7751809075"}|
|Data|{"id_contacto","123", "email:"dejahn@gmail.com", "telefono":"987654321"}|
|Versión|V1|
|Status Code|201 Created|
|Response Type|json|
|Response|{"id":"126", "name":"Mencho, "email":"mecnho@gmail.com"}|
|Curl|curl -X POST https://localhost:8000/contactos/123 -d {"email":"modificacion@gmail.com"}|
|Status Code (error)|409 Conflicto|
|Response Type(error)|JSON|
|Response (error)|{"error":"Contact already exists"}|

## 4.4 METODO DELETE

|Propiedad|Detalle|
|--|--|
|Descripción|EndPoint para eliminar un contacto en la API|
|Summary|EndPoint para eliminar un contacto|
|Metodo|DELETE|
|EndPoint|https://localhost:8000/contactos/{id}|
|Query Param|NA|
|Path Param|{id} int|
|Data|NA|
|Versión|V1|
|Status Code|202 No Content|
|Response Type|NA|
|Response|NA|
|Curl|curl -X DELETE https://localhost:8000/contactos/123|
|Status Code (error)|401 Not Fount|
|Response Type(error)|applicatio/json|
|Response (error)|{"error":"Contacto no encontrado"}|
