# Solicitudes HTTP con Requests
"""
Peticiones a otros servidores web desde Python.

En fakeapi.platzi.com es un servidor destinado para probar API web. Se pueden obtener diferentes listas.

pip install requests"
"""


import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # Ruta obtener datos
   
    print(r.status_code) # Estado del consumo 200 todo ok
    print(r.text) # Respuesta
    print(type(r.text)) # Tipo de dato - str

    # Transformar respuesta a json
    categorias = r.json()
    for categoria in categorias:
        print(categoria['name'])
