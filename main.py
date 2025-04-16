import subprocess
import sys
import os
from time import sleep

def instalar_yt_dlp():
    try:
        import yt_dlp
        print("A biblioteca yt-dlp já está instalada.")
    except ImportError:
        print("A biblioteca yt-dlp não está instalada. Instalando agora...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("yt-dlp instalado com sucesso!")

def get_pasta_videos():
    pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos")
    os.makedirs(pasta, exist_ok=True)
    return pasta

def baixar_playlist():
    try:
        instalar_yt_dlp()
        import yt_dlp

        url = input("Digite a URL da playlist: ").strip()
        pasta_destino = get_pasta_videos()

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': f'{pasta_destino}/%(playlist_title)s/%(title)s.%(ext)s',
            'noplaylist': False
        }

        print("Baixando playlist na melhor qualidade...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def baixar_video():
    try:
        instalar_yt_dlp()
        import yt_dlp

        url = input("Digite o URL do vídeo do YouTube: ").strip()
        pasta_destino = get_pasta_videos()

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s'
        }

        print("Baixando vídeo na melhor qualidade disponível...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

while True:
    estilo = 0
    while estilo not in [1, 2]:
        try:
            estilo = int(input('Quer baixar vídeo ou playlist?\n[1]: Vídeo\n[2]: Playlist\nSua resposta: '))
        except:
            estilo = 0
    if estilo == 1:
        baixar_video()
    else:
        baixar_playlist()
    sleep(1)
