# Proyecto USTREAM

## Descripción

Aplicación web con backend en Python y frontend estático. El backend expone una API para administrar videos y comentarios, y el frontend consume esas rutas para mostrar contenidos y reproducción.

## Requisitos

- Python 3.11 o superior.
- Entorno virtual para aislar dependencias.
- Dependencias incluidas en `BACKEND/requirements.txt`.

## Entorno virtual

1. Abrir la terminal en la carpeta del proyecto:
   ```powershell
   cd "d:\HTML\USTREAM"
   ```
2. Crear el entorno virtual:
   ```powershell
   python -m venv venv
   ```
3. Activar el entorno virtual:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
4. Instalar dependencias:
   ```powershell
   pip install -r BACKEND\requirements.txt
   ```

## Estructura del proyecto

- `BACKEND/` : Código del servidor y configuración de la base de datos.
- `BACKEND/main.py` : Aplicación FastAPI principal.
- `BACKEND/models.py` : Modelos de datos para videos y comentarios.
- `BACKEND/db.py` : Conexión y creación de tablas SQLite.
- `BACKEND/comments.py` : Operaciones auxiliares de comentarios.
- `BACKEND/app/routers/videos.py` : Rutas API para videos y comentarios.
- `BACKEND/db.sqlite3` : Base de datos local SQLite.
- `FRONTEND/` : Archivos HTML, CSS y JavaScript del cliente.
- `FRONTEND/index.html` : Página principal del frontend.
- `FRONTEND/stream.html` : Página de reproducción o transmisión.
- `FRONTEND/assets/` : Estilos y scripts del frontend.

## Dependencias principales

- `fastapi[standard]` : Framework para la API.
- `sqlmodel` : ORM para acceder a SQLite.

## Funcionalidades

- API REST para listar y crear videos.
- API para obtener recomendaciones por categoría.
- API para consultar y crear comentarios de videos.
- Base de datos SQLite local para persistencia.
- Frontend estático que consume la API y muestra contenido.

## Ejecución

1. Activar el entorno virtual.
2. Iniciar el backend desde la raíz del proyecto:
   ```powershell
   python -m uvicorn BACKEND.main:app --reload --host 127.0.0.1 --port 8000
   ```
3. Abrir el frontend en el navegador desde `FRONTEND/index.html` o servirlo con otra herramienta estática.

## Uso básico

- Acceder a `http://127.0.0.1:8000/videos` para ver la lista de videos.
- Acceder a `http://127.0.0.1:8000/videos/{id}` para ver un video por ID.
- Acceder a `http://127.0.0.1:8000/videos/recomendaciones/{categoria}` para obtener recomendaciones.
- Enviar comentarios mediante `POST /comments`.

## Ajuste de la ruta raíz

Si la carpeta del proyecto cambia de nombre, actualizar la ruta usada en la terminal para apuntar a la nueva ubicación.
