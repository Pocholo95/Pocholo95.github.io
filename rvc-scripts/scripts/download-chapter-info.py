import subprocess

# Preguntar la URL del video
url = input("Ingrese la URL del video: ")

# Construir el comando yt-dlp con la URL proporcionada
command = f'yt-dlp -x --audio-format wav --audio-quality 0 "{url}" -o "%(title)s.%(ext)s" --split-chapters -o "chapter:%(title)s/[%(section_number)s] - %(section_title)s.%(ext)s"'

# Ejecutar el comando en la consola
subprocess.run(command, shell=True)
