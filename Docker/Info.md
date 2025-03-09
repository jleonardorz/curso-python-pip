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

3. Correr el docket se crea el archivo `docker-compose.yml` - declara como se inicia el contenedor

   services:   - crea un servicio
   app-csv:    - nombre del servicio
      build:   
         context: . - carpeta actual 
         dockerfile: Dockerfile  - Use el archivo

