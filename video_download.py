from pytube import YouTube

def download_video(url, output_path="."):
    yt = YouTube(url)
    video = yt.streams.first()
    video.download(output_path)

url = "https://youtube.com/shorts/S0sXj7oFRaI?si=CFobXTHfWTDyg0p0"
download_video(url)