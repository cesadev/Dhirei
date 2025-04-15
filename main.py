import subprocess
import sys
from time import sleep

def instalar_yt_dlp():
    try:
        # Verifica se a biblioteca yt_dlp está instalada
        import yt_dlp
        print("A biblioteca yt-dlp já está instalada.")
    except ImportError:
        # Caso não esteja instalada, instala automaticamente
        print("A biblioteca yt-dlp não está instalada. Instalando agora...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("yt-dlp instalado com sucesso!")

def baixar_playlist():
    try:
        instalar_yt_dlp()  # Verifica ou instala yt-dlp antes de iniciar
        import yt_dlp

        # Solicita o URL da playlist ao usuário
        url = input("Enter the URL of the YouTube playlist: ").strip()
        pasta_destino = input("Enter the folder path where you want to save the videos (or press Enter to use the current directory): ")
        if not pasta_destino.strip():
            pasta_destino = "."  # Usa o diretório atual como padrão

        # Configuração para baixar vídeos da playlist
        ydl_opts = {
            'format': 'best',  # Baixa o melhor formato único disponível (vídeo com áudio integrado)
            'outtmpl': f'{pasta_destino}/%(playlist_title)s/%(title)s.%(ext)s',  # Organiza em subpastas com o nome da playlist
            'noplaylist': False  # Certifica que a playlist será baixada
        }

        print("Downloading playlist...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Playlist download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def baixar_video():
    try:
        instalar_yt_dlp()  # Verifica ou instala yt-dlp antes de iniciar
        import yt_dlp

        url = input("Digite o URL do vídeo do YouTube: ").strip()
        pasta_destino = input("Digite o caminho da pasta onde deseja salvar o vídeo (ou pressione Enter para usar a pasta atual): ")
        if not pasta_destino.strip():
            pasta_destino = "."  # Define a pasta atual como padrão

        # Configuração para baixar apenas o melhor formato único disponível
        ydl_opts = {
            'format': 'best',  # Baixa o melhor formato único disponível (vídeo com áudio)
            'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s'
        }

        print("Baixando o melhor formato disponível...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

while True:
    estilo = 0
    while estilo not in [1, 2]:
        estilo = int(input('Quer baixar vídeo ou playlist?\n[1]:Vídeo\n[2]:Playlist\nSua resposta: '))
    if estilo == 1:
        baixar_video()
    elif estilo == 2:
        baixar_playlist()
    sleep(1)