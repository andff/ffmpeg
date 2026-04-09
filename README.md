# Códigos ffmpeg

Todos utilizados no Prompt de Comandos (DOS) ou PowerShell


## Baixe e instale (Download)

<a href="https://ffmpeg.org/download.html" target="_blank">https://ffmpeg.org/download.html</a>

## Instalar usando Winget
```
winget install Gyan.FFmpeg
```

```
winget install Gyan.FFmpeg.Essentials
```

## Verificar instalacion
```
ffmpeg -version
```

## Todas as informações do video
```
ffmpeg -i video.mp4
```

## Converter video em outro formato
```
ffmpeg -i entrada.mp4 saida.avi
```

## Extrair áudio de um vídeo
```
ffmpeg -i video.mp4 audio.mp3
```

## Cortar um trecho de vídeo
```
ffmpeg -i video.mp4 -ss 00:00:10 -to 00:00:30 -c copy corte.mp4
```

## Reduzir tamanho (compressão)
```
ffmpeg -i video.mp4 -vcodec libx264 -crf 28 video_comprimido.mp4
```

## Redimensionar vídeo
```
ffmpeg -i video.mp4 -vf scale=1280:720 video_720p.mp4
```

## Converter video em outro formato com qualidade
```
ffmpeg -i entrada.mp4 -q:v 0 saida.avi
```

## Remover áudio de um vídeo
```
ffmpeg -i video.mp4 -an sem_audio.mp4
```

## Juntar vídeos

Crie um arquivo lista.txt assim:

file 'video1.mp4'
file 'video2.mp4'
file 'video3.mp4'

depois execute:
```
ffmpeg -f concat -safe 0 -i lista.txt -c copy final.mp4
```
Requisitos: Todos os vídeos devem ter mesmo formato, resolução e codec

## Juntar vídeos - Método alternativo (funciona sempre)
```
ffmpeg -i video1.mp4 -i video2.mp4 -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1" output.mp4
```

## Adicionar legendas
```
ffmpeg -i video.mp4 -vf subtitles=legenda.srt video_leg.mp4
```

## Legenda “opcional” (ativável no player)
```
ffmpeg -i video.mp4 -i legenda.srt -c copy -c:s mov_text video_com_legenda.mp4
```

## Criar GIF
### método simples
```
ffmpeg -i video.mp4 -ss 00:00:05 -t 5 gif.gif
```
### Método profissional (melhor qualidade)
```
ffmpeg -i video.mp4 -ss 00:00:05 -t 5 -vf "fps=10,scale=480:-1:flags=lanczos,palettegen" palette.png

ffmpeg -i video.mp4 -i palette.png -ss 00:00:05 -t 5 -lavfi "fps=10,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" gif_final.gif
```
Dicas para gifs 
Use -crf 23 (qualidade boa) ao converter
Use -preset fast para acelerar
Use -an se quiser remover áudio
Use -r 10 para controlar FPS no GIF


## Converter video em outro formato com qualidade e sem audio
```
ffmpeg -i entrada.mp4 -q:v 0 -an saida.avi
```

## Converter video em outro formato com qualidade e sem audio e com outra resolução
```
ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 saida.avi
```

## Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros
```
ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 saida.avi
```

## Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec
```
ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 saida.avi
```

## Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio
```
ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac saida.avi
```

## Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio e com outro codec de audio
```
ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac -c:s mov_text saida.avi
```

## Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio e com outro codec de audio e com outro codec de audio
```
ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac -c:s mov_text -c:a:0 aac -c:a:1 aac saida.avi
```

## Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio
```
ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac -c:s mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text saida.avi
```

## Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio
```
ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac -c:s mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text saida.avi
```

## Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio
```
ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac -c:s mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text saida.avi
```
