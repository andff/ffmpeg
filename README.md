# ffmpeg
ffmpeg

# Instalar

```winget install Gyan.FFmpeg```
```winget install Gyan.FFmpeg.Essentials```

# Verificar instalacion

```ffmpeg -version```

# Converter video em outro formato

ffmpeg -i entrada.mp4 saida.avi

# Converter video em outro formato com qualidade

ffmpeg -i entrada.mp4 -q:v 0 saida.avi

# Converter video em outro formato com qualidade e sem audio

ffmpeg -i entrada.mp4 -q:v 0 -an saida.avi

# Converter video em outro formato com qualidade e sem audio e com outra resolução

ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 saida.avi

# Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros

ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 saida.avi

# Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec

ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 saida.avi

# Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio

ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac saida.avi

# Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio e com outro codec de audio

ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac -c:s mov_text saida.avi

# Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio e com outro codec de audio e com outro codec de audio

ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac -c:s mov_text -c:a:0 aac -c:a:1 aac saida.avi

# Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio

ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac -c:s mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text saida.avi

# Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio

ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac -c:s mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text saida.avi

# Converter video em outro formato com qualidade e sem audio e com outra resolução e com outra taxa de quadros e com outro codec e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio e com outro codec de audio

ffmpeg -i entrada.mp4 -q:v 0 -an -s 1280x720 -r 30 -c:v libx264 -c:a aac -c:s mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text -c:a:0 aac -c:a:1 aac -c:s:0 mov_text -c:s:1 mov_text saida.avi
