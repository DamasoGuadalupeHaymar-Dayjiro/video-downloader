import customtkinter as ctk
from tkinter import messagebox
import yt_dlp
import os

# ---------------- CONFIGURACIÓN ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


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

def iniciar():
    url = entrada.get().strip()

    if not url:
        messagebox.showerror("Error", "Ingresa una URL")
        return

    try:
        if opcion.get() == "mp4":
            estado.configure(text="Descargando video...")
            descargar_video(url)

        else:
            estado.configure(text="Descargando audio...")
            descargar_audio(url)

        estado.configure(text="Descarga completada ✔")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- INTERFAZ ----------------

app = ctk.CTk()
app.title("Downloader Pro")
app.geometry("500x350")
app.resizable(False, False)

# Título
titulo = ctk.CTkLabel(app, text="Descargador de Videos", font=("Arial", 20, "bold"))
titulo.pack(pady=15)

# Entrada URL
entrada = ctk.CTkEntry(app, width=400, placeholder_text="Pega aquí la URL del video")
entrada.pack(pady=10)

# Opciones
opcion = ctk.StringVar(value="mp4")

frame = ctk.CTkFrame(app)
frame.pack(pady=10)

radio_mp4 = ctk.CTkRadioButton(frame, text="Video MP4", variable=opcion, value="mp4")
radio_mp4.pack(side="left", padx=20)

radio_mp3 = ctk.CTkRadioButton(frame, text="Audio MP3", variable=opcion, value="mp3")
radio_mp3.pack(side="right", padx=20)

# Botón
boton = ctk.CTkButton(app, text="DESCARGAR", command=iniciar)
boton.pack(pady=20)

# Estado
estado = ctk.CTkLabel(app, text="Listo", font=("Arial", 12))
estado.pack(pady=10)

app.mainloop()
