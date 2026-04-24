import yt_dlp

def descargar_video(url):
    opciones = {
        'outtmpl': 'videos/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best'
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


def descargar_audio(url):
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
