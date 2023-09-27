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
