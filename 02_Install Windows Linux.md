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
