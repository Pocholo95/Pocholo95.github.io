@echo off
chcp 65001 > nul
setlocal EnableDelayedExpansion

:menu
cls
echo 1. Descargar video por capítulos.
echo 2. Descargar video por capitulos (txt).
echo 3. Recortar audio.
echo 4. Generar informacion de capitulos.
echo 5. Salir

set /p choice=Elige una opción: 

if "%choice%"=="1" (
    call :opcion1
) else if "%choice%"=="2" (
    call :opcion2
) else if "%choice%"=="3" (
    call :opcion3
) else if "%choice%"=="4" (
    call :opcion4
) else if "%choice%"=="5" (
    exit /b
) else (
    echo Opción no válida. Inténtalo de nuevo.
    pause
    goto :menu
)

:opcion1
echo Ejecutando Descarga de video por capítulos...
rem
python scripts/download-chapter-info.py
pause
goto :menu

:opcion2
echo Ejecutando Descarga de video por capítulos (txt)...
rem
python scripts/download-chapter-info-txt.py
pause
goto :menu

:opcion3
echo Ejecutando Recortar audios...
rem
python scripts/audio-cropper.py
pause
goto :menu

:opcion4
echo Generar info de caps (txt)...
rem
python scripts/generate-info-from-txt.py
pause
goto :menu
