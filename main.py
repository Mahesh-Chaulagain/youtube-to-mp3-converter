import yt_dlp

url = input('Enter video URL: ')

yt_opts = {
    'format': 'bestaudio/best',  # Downloads the best audio format available
    'noplaylist': True,  # Avoid downloading playlists
}

with yt_dlp.YoutubeDL(yt_opts) as ydl:
    ydl.download([url])

print('Audio downloaded successfully (in original format).')


# import pytube

# try:
#     # set video url
#     url = input("Enter your URL: ")

#     # create Youtube object
#     video = pytube.YouTube(url)

#     # download video and convert to mp3
#     stream = video.streams.filter(only_audio=True).first()
#     print("Audio is being downloaded")

#     # download file
#     stream.download()

#     print("Download complete!")

# except Exception as e:
#     print(f"An error occurred: {str(e)}")


