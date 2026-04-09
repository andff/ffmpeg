import subprocess

subprocess.run([
    "ffmpeg",
    "-i", "video.mp4",
    "video.avi"
])