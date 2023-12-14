import subprocess
import os

# Preguntar la URL del video
url = input("Ingrese la URL del video: ")

# Obtener la ruta del script y la carpeta raíz
script_directory = os.path.dirname(os.path.realpath(__file__))
root_directory = os.path.dirname(script_directory)

# Construir la ruta del archivo JSON en la misma carpeta que el script
json_file_path = os.path.join(script_directory, 'chapters.json')

# Verificar si el archivo JSON existe
if not os.path.isfile(json_file_path):
    print("Error: No se encontró el archivo 'chapters.json' en la misma carpeta del script.")
    exit()

# Construir el comando yt-dlp con la URL proporcionada y la información de los capítulos
command = (
    f'yt-dlp -x --audio-format wav --audio-quality 0 "{url}" '
    f'-o "{root_directory}/%(title)s.%(ext)s" '
    f'--split-chapters -o "chapter:{root_directory}/%(title)s/[%(section_number)s] - %(section_title)s.%(ext)s" '
    f'--replace-in-metadata pre_process "chapters" "{json_file_path}"'
)

# Ejecutar el comando en la consola
subprocess.run(command, shell=True)
