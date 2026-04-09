# Estrutura da pasta
 
# seu_script.py
# /videos
#    video1.mp4
#    video2.mp4
#    video3.mp4

# Todos os vídeos precisam ter: mesma resolução, mesmo codec, mesmo FPS




import os
import subprocess

# Pasta onde estão os vídeos
pasta_videos = "videos"  # pode mudar

# Nome do arquivo de saída
saida = "final.mp4"

# Extensões suportadas
extensoes = (".mp4", ".avi", ".mkv", ".mov")

# Lista os vídeos
videos = [f for f in os.listdir(pasta_videos) if f.lower().endswith(extensoes)]

# Ordena os vídeos (IMPORTANTE)
videos.sort()

# Caminho do arquivo lista
lista_path = os.path.join(pasta_videos, "lista.txt")

# Cria o arquivo lista.txt
with open(lista_path, "w", encoding="utf-8") as f:
    for video in videos:
        caminho = os.path.join(pasta_videos, video)
        f.write(f"file '{caminho}'\n")

print(f"{len(videos)} vídeos encontrados.")

# Comando FFmpeg
comando = [
    "ffmpeg",
    "-f", "concat",
    "-safe", "0",
    "-i", lista_path,
    "-c", "copy",
    saida
]

# Executa o comando
subprocess.run(comando)

print("Vídeos unidos com sucesso!")