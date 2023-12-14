import re
import json
import os

# Obtener la ruta absoluta del archivo chapters.txt
file_name = 'chapters.txt'
file_path = os.path.abspath(file_name)

with open(file_path, 'r', encoding='utf-8') as file:
    datos = file.read()

# Separar líneas y extraer tiempo y título
lineas = datos.strip().split('\n')
capitulos = []

for linea in lineas:
    match1 = re.match(r'(.+) (\d{2}:\d{2}:\d{2})$', linea)
    match2 = re.match(r'(\d{2}:\d{2}:\d{2}) (.+)$', linea)
    match3 = re.match(r'(\d{2}:\d{2}) (.+)$', linea)

    if match1:
        titulo, tiempo = match1.groups()
        capitulos.append({"title": titulo, "start_time": tiempo})
    elif match2:
        tiempo, titulo = match2.groups()
        capitulos.append({"title": titulo, "start_time": tiempo})
    elif match3:
        tiempo, titulo = match3.groups()
        capitulos.append({"title": titulo, "start_time": tiempo})

# Obtener la ruta del script y la carpeta raíz
script_directory = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta del archivo JSON en la misma carpeta que el script
json_file_name = 'chapters.json'
json_file_path = os.path.join(script_directory, json_file_name)

# Escribir la lista de capítulos en el archivo JSON
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(capitulos, json_file, indent=2, ensure_ascii=False)

print(f'Se han generado los capítulos en el archivo {json_file_path}.')
