# Windows con WSL  / Ubuntu

1. Con la terminal de Ubuntu
2. Por defecto python3

1. PowerShell wsl --install
2. Al terminar se reinicia el computador
3. Al reiniciar entra en la configuración de Ubuntu
4. Ingresar username y password

1. Entrar a la Terminal
2. Abrir una pestaña con Ubuntu


1. sudo apt update
2. sudo apt -y upgrade
3. python3 -V - verificar la versión

### Instalar paquete de gestor de dependencias

1. sudo apt install -y python3-pip
2. pip3 -V
3. Depedencias 
    apt install -y build-essential libssl-dev libffi-dev python3-dev

### Windows nativo

1. pip --version - por lo general ya viene instalado
2. En caso que no python -m ensurepip --default-pip

1. Descargar https://visualstudio.microsoft.com/es/visual-cpp-build-tools/ para build-essential
2. pip install cryptography para libssl-dev y libffi-dev
3. python3-dev instlar python con la opcion de desarrollo
    Verificar con:
    python -c "import sysconfig; print(sysconfig.get_paths()['include'])"

    Debe aparecer la carpeta Include

    ejecutar:
    pip install --upgrade setuptools wheel
    pip install --verbose cffi


## Extenciones VSCODE

1. python for microsoft
2. Si esta con WSL -> WSL for microsoft

Abrir un proyecto en VSCODE
1. en WSL
2. mkdir proyecto
3. cd proyecto
4. code .


## Repositorio en Git

1. POr web crear un repositorio : + > New Repository
2. Nombre repositorio
3. Repositorio publico
4. Crear repositorio
5. Link conexión 

git remote add origin https://github.com/..............

6. Estando en la carpeta del proyecto desde la terminal de Bash Git
7. git init -> Inicializa el repositorio
8. link conexion
    git remote add origin https://github.com/............
9. Verificar enlace git remote -v


**Configuracion git para identidad**

1. Terminal bash Git
2. git config --global user.name "Tu Nombre"
   git config --global user.email "tuemail@example.com"
3. Verificar configuracion
    git config --global --list


**Cambios sincronizar**

1. git add *   - Inicia seguimiento al archivo
2. git commit -m "Mi primer archivo"  - Envia cambio a la BD sistema
3. git push origin master  - Pasar cambios al servidor remoto
4. Ya quedan subidos en GitHub


**Hacer un repo profesional**

1. En gitinore io - https://www.toptal.com/developers/gitignore
    Archivos que deberían ignorarse y no deben ser parte del repositorio
2. En el pront: Windows Linux macOs Python 
3. Dar en Create
4. Copiar archivo
5. en VS Code crear archivo .gitignore

6. Crear archivo README.md
    Instrucciones que quiera trabar con el proyecto
7. Se deja inicializado con
    `# Steps`



### Commit cambios

1. git add *
2. git commit -m "add files"
3. git push origin master

