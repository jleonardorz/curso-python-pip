# Docker

Plataforma que permite crear, distribuir y ejecutar aplicaciones en contenedores.

Contenedor: paquete ligero y portátil que incluye
- Código de la aplicación
- Dependencias necesarias (librerías, frameworks)
- Configuración de Sistema Operativo

Esto permite que la aplicación funcione igual en cualquier entorno: local, servidores, nube.

- Cada contenedor es independiente y no afecta al resto del sistema
- facilita el despliegue
- menos consumo de recursos en maquinas virtuales

Aísla el entorno de ejecución (no solo las dependencias o librerías)



# Instalar Docker

1. Descargar/Instalar https://docs.docker.com/desktop/setup/install/windows-install/


2. Habilitar Hyper-V de Windows mediante Agregar Características de Windows
   WIndows Home Habitar "Plataforma de maquina Virtual"

   ó

   wsl

   https://platzi.com/tutoriales/2042-prework-windows/7874-guia-de-instalacion-de-wsl-v2-y-windows-terminal/
    


# Aplicaciones en Docket

## De scripts CSV

1. Crear nuevo archivo `Dockerfile`
2. Se edita el archivo con

   FROM python:3.13              - Versión de python - Crea Contenedor
   WORKDIR /csv                  - carpeta contenedor - aplicacion
   COPY requirements.txt /csv/requirements.txt    - se copia el archivo de requerimientos COPY local contenedor

   RUN pip install --no-cache-dir -r --upgrade /csv/requirements.txt   - Instala dependencias y actializa pip

   COPY . /csv/    - Copie todo . hacia la carpeta del contenedor

   CMD bash -c "while true; do sleep 1; done"     - mantener el contendedor funcionando

3. Correr el docket se crea el archivo `docker-compose.yml` - declara como se inicia el contenedor

   services:   - crea un servicio
   app-csv:    - nombre del servicio
      build:   
         context: . - carpeta actual 
         dockerfile: Dockerfile  - Use el archivo

4. En la terminal de WSL dentro de la carpeta del proyecto
   docker-compose build

5. lanzar, deberá indicar Creado e Iniciado
   docker-compose up -d

6. Ver el estado del contenedor - debe aparecer el nombre del contendedor y en estado Corriendo
   docker-compose ps

7. Ingresar al ambiente forma 1
   docker-compose exec app-csv bash  (ejecute nombre_servicio conecta_con_bash)

   Cambia el pront, ya estamos dentro del contenedor -> Es como si se conectara a un servidor en la nube  Unix

   Ya se puede ejecutar python main.py


## Enlazar el sistema de archivos local con el del contenedor

1. En el archivo `docker-compose.yml` se agrega la linea debajo de bulding

   volumes:
      - .:/csv

2. En terminal dentro de la carpeta del proyecto
   docker-compose  up -d  - Recrea el contenedor

3. Ingreso al contenedor
   docker-compose exec app-csv bash


# Contenedor de WebServices FastAPI

1. Crear nuevo archivo `Dockerfile`
2. Se edita el archivo con

   FROM python:3.13              - Versión de python - Crea Contenedor
   WORKDIR /web-serverFastAPI                  - carpeta contenedor - aplicacion
   COPY requirements.txt /web-serverFastAPI/requirements.txt    - se copia el archivo de requerimientos COPY local contenedor

   RUN pip install --no-cache-dir -r --upgrade /web-serverFastAPI/requirements.txt   - Instala dependencias y actializa pip

   COPY . /web-serverFastAPI/    - Copie todo . hacia la carpeta del contenedor

   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8043"]     - Inicia el servidor con uvicorn

3. Correr el docket se crea el archivo `docker-compose.yml` - declara como se inicia el contenedor

   services:   - crea un servicio
   app-web-serverFastAPI:    - nombre del servicio
      build:   
         context: . - carpeta actual 
         dockerfile: Dockerfile  - Use el archivo
      volumes:
      - .:/web-serverFastAPI   - para sincronizar directorios
      ports:
      - '8043:8043'  - conectar el puerto mi maquina: con el contenedor

4. Dentro de la carpeta del proyecto 
   docker-compose build
   docker-compose up -d
   docker-compose ps

5. En el navegador ingresar a http://localhost:8043/


Con http://localhost:8043/docs ingresa a la documentacion
Con http://localhost:8043/redoc ingresa a redoc


