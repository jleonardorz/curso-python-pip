# WebServices con FastAPI
"""
FastAPI es un framework para construir APIs RESTFul.

Muy eficiente tipo asíncrono y esta basado en Starlette y Pydantic lo que permite
validaciones automáticas y documentación interactiva.

Crear mi propio servidor web

Compatible con OpenAPI y JSON Schema

pip install fastapi  # Librería
pip install "uvicorn[standard]"  # Servidor web para publicar el servicio

"""

# Lanzar el servidor
"""
Terminal
1. uvicorn archivo:nombre_aplicacion --reload  - uvicorn main:app --reload
2. Entrega la IP par poner en navegador
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Instancia de aplicación
app = FastAPI()

# Recurso
@app.get('/') # Ruta que se accede desde la web
def get_list():
    return [1,2,3,4]


@app.get('/contact') # Ruta que se accede desde la web
def get_list():
    return {'name': 'Platzi'}

# Devolver HTML
@app.get('/contact_html', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>Y soy un párrafo</p>
    """


def run():
    pass

if __name__ == '__main__':
    run()
