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

pasta_entrada = "videos"
pasta_convertidos = "convertidos"
saida = "final.mp4"

extensoes = (".mp4", ".avi", ".mkv", ".mov", ".flv")

os.makedirs(pasta_convertidos, exist_ok=True)

videos = [f for f in os.listdir(pasta_entrada) if f.lower().endswith(extensoes)]
videos.sort()

print(f"{len(videos)} vídeos encontrados.\n")

# 🔍 Detectar encoder disponível
def detectar_encoder():
    try:
        resultado = subprocess.check_output(["ffmpeg", "-encoders"], text=True)

        if "h264_nvenc" in resultado:
            return "h264_nvenc"
        elif "h264_amf" in resultado:
            return "h264_amf"
        else:
            return "libx264"
    except:
        return "libx264"

encoder = detectar_encoder()
print(f"Encoder selecionado: {encoder}\n")

videos_convertidos = []

# 🔄 CONVERSÃO
for i, video in enumerate(videos):
    entrada = os.path.join(pasta_entrada, video)
    nome_saida = f"video_{i:03d}.mp4"
    saida_convertida = os.path.join(pasta_convertidos, nome_saida)

    print(f"Convertendo: {video}")

    if encoder == "h264_nvenc":
        comando = [
            "ffmpeg", "-i", entrada,
            "-vf", "scale=1280:720,fps=30",
            "-c:v", "h264_nvenc",
            "-preset", "fast",
            "-b:v", "2M",
            "-c:a", "aac",
            "-b:a", "128k",
            "-y",
            saida_convertida
        ]

    elif encoder == "h264_amf":
        comando = [
            "ffmpeg", "-i", entrada,
            "-vf", "scale=1280:720,fps=30",
            "-c:v", "h264_amf",
            "-b:v", "2M",
            "-c:a", "aac",
            "-b:a", "128k",
            "-y",
            saida_convertida
        ]

    else:
        # fallback CPU
        comando = [
            "ffmpeg", "-i", entrada,
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

# 📄 lista.txt
lista_path = os.path.join(pasta_convertidos, "lista.txt")

with open(lista_path, "w", encoding="utf-8") as f:
    for v in videos_convertidos:
        f.write(f"file '{v}'\n")

print("\nJuntando vídeos...")

# 🔗 CONCAT
subprocess.run([
    "ffmpeg",
    "-f", "concat",
    "-safe", "0",
    "-i", lista_path,
    "-c", "copy",
    saida
])

print("\n✅ Finalizado com sucesso!")