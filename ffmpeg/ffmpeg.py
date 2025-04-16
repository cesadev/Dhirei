import os
import zipfile
import requests
import shutil

def baixar_ffmpeg_windows(destino='ffmpeg'):
    url = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip'
    nome_zip = 'ffmpeg.zip'

    print('[+] Baixando FFmpeg...')
    with requests.get(url, stream=True) as r:
        with open(nome_zip, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    print('[+] Extraindo...')
    with zipfile.ZipFile(nome_zip, 'r') as zip_ref:
        zip_ref.extractall(destino)

    # Move bin para a raiz do destino
    subpastas = os.listdir(destino)
    for pasta in subpastas:
        if 'ffmpeg' in pasta and os.path.isdir(os.path.join(destino, pasta)):
            bin_path = os.path.join(destino, pasta, 'bin')
            for file in os.listdir(bin_path):
                shutil.move(os.path.join(bin_path, file), '.')
            break

    os.remove(nome_zip)
    print('[+] FFmpeg baixado e pronto para uso!')

# Exemplo de uso:
baixar_ffmpeg_windows()
