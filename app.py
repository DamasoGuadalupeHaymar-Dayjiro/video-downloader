import tkinter as tk
from tkinter import messagebox
import yt_dlp
import os

# ---------------- DESCARGA ----------------

def descargar_video(url):
    os.makedirs("videos", exist_ok=True)

    opciones = {
        'outtmpl': 'videos/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best'
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


def descargar_audio(url):
    os.makedirs("audios", exist_ok=True)

    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': 'audios/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


# ---------------- LÓGICA ----------------

def iniciar_descarga():
    url = entrada.get().strip()

    if not url:
        messagebox.showerror("Error", "Por favor ingresa una URL")
        return

    try:
        if opcion.get() == "mp4":
            estado.set("Descargando video...")
            ventana.update()
            descargar_video(url)

        else:
            estado.set("Descargando audio...")
            ventana.update()
            descargar_audio(url)

        estado.set("Descarga completada ✔")
        messagebox.showinfo("Éxito", "Descarga finalizada")

    except Exception as e:
        estado.set("Error en la descarga")
        messagebox.showerror("Error", str(e))


# ---------------- INTERFAZ ----------------

ventana = tk.Tk()
ventana.title("Downloader Pro")
ventana.geometry("450x300")
ventana.resizable(False, False)

# Título
titulo = tk.Label(ventana, text="Descargador de Videos", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Entrada URL
tk.Label(ventana, text="Ingresa la URL del video:").pack()

entrada = tk.Entry(ventana, width=55)
entrada.pack(pady=5)

# Opciones
opcion = tk.StringVar(value="mp4")

frame = tk.Frame(ventana)
frame.pack(pady=10)

tk.Radiobutton(frame, text="Video MP4", variable=opcion, value="mp4").pack(side="left", padx=20)
tk.Radiobutton(frame, text="Audio MP3", variable=opcion, value="mp3").pack(side="right", padx=20)

# Botón principal
boton = tk.Button(
    ventana,
    text="DESCARGAR",
    command=iniciar_descarga,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=2
)
boton.pack(pady=15)

# Estado
estado = tk.StringVar()
estado.set("Listo para descargar")

label_estado = tk.Label(ventana, textvariable=estado, fg="blue")
label_estado.pack(pady=10)

ventana.mainloop()
