@echo off

rem Verificar se o Python está instalado
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python não está instalado. Por favor, instale o Python antes de continuar.
    pause
    exit /b
)

rem Definir o diretório do arquivo Python
set "python_script_dir=%~dp0"

rem Executar o código Python
python "%python_script_dir%cextension-GUI.py"
