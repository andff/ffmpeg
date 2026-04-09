# Estrutura da pasta
 
# seu_script.py
# /videos
#    video1.mp4
#    video2.mp4
#    video3.mp4

# /convertidos (criada automaticamente)
# /final.mp4

import os
import subprocess

# Pasta com vídeos originais
pasta_entrada = "videos"

# Pasta temporária para vídeos convertidos
pasta_convertidos = "convertidos"

# Arquivo final
saida = "final.mp4"

# Extensões aceitas
extensoes = (".mp4", ".avi", ".mkv", ".mov", ".flv")

# Cria pasta de convertidos se não existir
os.makedirs(pasta_convertidos, exist_ok=True)

# Lista vídeos
videos = [f for f in os.listdir(pasta_entrada) if f.lower().endswith(extensoes)]
videos.sort()

print(f"{len(videos)} vídeos encontrados.\n")

videos_convertidos = []

# 🔄 CONVERSÃO
for i, video in enumerate(videos):
    entrada = os.path.join(pasta_entrada, video)
    nome_saida = f"video_{i:03d}.mp4"
    saida_convertida = os.path.join(pasta_convertidos, nome_saida)

    print(f"Convertendo: {video} → {nome_saida}")

    comando = [
        "ffmpeg",
        "-i", entrada,
        "-vf", "scale=1280:720,fps=30",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "128k",
        "-y",
        saida_convertida
    ]

    subprocess.run(comando)

    videos_convertidos.append(saida_convertida)

# 📄 CRIA lista.txt
lista_path = os.path.join(pasta_convertidos, "lista.txt")

with open(lista_path, "w", encoding="utf-8") as f:
    for video in videos_convertidos:
        f.write(f"file '{video}'\n")

print("\nTodos os vídeos convertidos!\n")

# 🔗 JUNTA OS VÍDEOS
print("Juntando vídeos...")

comando_concat = [
    "ffmpeg",
    "-f", "concat",
    "-safe", "0",
    "-i", lista_path,
    "-c", "copy",
    saida
]

subprocess.run(comando_concat)

print("\n✅ Vídeo final criado com sucesso!")