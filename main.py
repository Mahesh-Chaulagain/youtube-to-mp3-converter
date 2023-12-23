import pytube

# set video url
url = "https://www.youtube.com/watch?v=5tW6Yj-E2Wk"

# create Youtube object
video = pytube.YouTube(url)

# download video and convert to mp3
stream = video.streams.filter(only_audio=True).first()

# download file
stream.download(filename=f"{video.title}.mp3")

