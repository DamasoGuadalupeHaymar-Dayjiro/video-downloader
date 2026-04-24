from downloader.youtube_downloader import descargar_video, descargar_audio
from utils.validator import es_url_valida
import os

url = input("Ingresa la URL: ")

if not es_url_valida(url):
    print("URL inválida")
    exit()

print("1. Video")
print("2. Audio")

opcion = input("Opción: ")

if opcion == "1":
    if not os.path.exists("videos"):
        os.makedirs("videos")
    descargar_video(url)

elif opcion == "2":
    if not os.path.exists("audios"):
        os.makedirs("audios")
    descargar_audio(url)

else:
    print("Opción no válida")
