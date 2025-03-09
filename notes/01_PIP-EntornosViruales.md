# PIP y Entornos Virtuales

## PIP

pip (Package Installer for Python) es el administrador de paquetes de Python. Permite instalar, actualizar y administrar bibliotecas y dependencias desde el repositorio PyPI (Python Package Index).

> Ecosistema: librerías o framework que ya existen.

En pypi.org se encuentran toda la información.

**Usos**
- Instalar paquetes de terceros
- Actualizar paquetes instalados
- Desinstalar paquetes
- Ver lista de paquetes instalados

### Comandos básicos

1. Instalar paquete `pip install nombre_paquete`
2. Instalar una versión especifica `pip install nombre_paquete==version`
3. Actualizar `pip install --upgrade nombre_paquete`
4. Desinstalar paquete `pip uninstall nombre_paquete`
5. Listar paquetes `pip list`
6. Ver información paquete instalado `pip show nombre_paquete`
7. Instalar paquete desde archivo `pip install -r requeriments.txt`
8. Ver entorno de Python `pip freeze`

## Ambientes virtuales

Es un entorno aislado donde puedes instalar paquetes sin afectar la instalación global de python.

Esto permite:
- Trabajar en diferentes proyectos con distintas versiones de paquetes
- Evitar conflictos entre dependencias
- Mantener tu instalación global de Python limpia.

Cuando se instala un pip queda en el ambiente global de Python y puede causar algunos problemas como:
- Pueden cruzar las configuraciones
- Las versiones de las pip en los diferentes proyectos puede ser diferente
- Cada proyecto puede tener sus propios módulos

El ambiente virtual encapsula cada modulo para cada proyecto, con sus propias dependencias y versiones para que no choquen unas con otras.

### Crear ambiente virtual

- Esto creara una carpeta mi_entorno con el entorno virtual.
- Al activarlo el promt del terminal cambia, indicando que estás dentro del entorno virtual.
- La instalación de paquetes se hace como de costumbre.

**Windows**
1. where python - saber donde se esta ejecutando
    D:\DEV\SW\Python\Python313\python.exe -> Global
2. En la carpeta del proyecto
3. python -m venv mi_entorno
4. mi_entorno\Scripts\activate
5. Al ejecutar where python o where pip, cambia la ruta
    D:\DEV\Proyectos\PythonCurso\02_ PIP_Entornos_Virtuales\csv\env\Scripts\python.exe
6. Al ejecutar pip freeze aparece vació - por lo que hay que instalar los módulos necesarios

Para activar las politicas error en terminal
PowerShell como adminstrador
1. Get-ExecutionPolicy -list - ver lista de politicas
2. Set-ExecutionPolicy RemoteSigned -Force - Activar politica
3. Desactivarlo Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope LocalMachine


Solo para la secion actual por seguridad
1. Set-ExecutionPolicy RemoteSigned -Scope Process

**Linux**
1. which python3 - donde se esta ejecutando
2. python3 -m venv mi_entorno
3. source mi_entorno/bin/activate

Para desactivar el ambiente virtual con 
deactivate

Para eliminar se puede manual:
- Linux: rm -rf mi_entorno
- Windows: rmdir /s /q mi_entorno

#### archivo requirements.txt

Ayuda a mantener las dependencias y módulos, y que versiones necesita para correr el proyecto de forma optima, en vez de instalar manualmente, denominado `requirements.txt`

1. Entrar a la carpeta del proyecto
2. Entrar al entorno virtual
3. El resultado del comando `pip freeze` se convierte en un txt
 - Windows: pip freeze > requirements.txt
 - Linux: pip3 freeze > requirements.txt

Luego para instalar las dependencias
1. pip install -r requirements.txt
