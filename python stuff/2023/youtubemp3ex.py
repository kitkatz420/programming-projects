from pytube import YouTube

# creating YouTube object
yt = YouTube(input("what is your url")) 

# accessing audio streams of YouTube obj.(first one, more available)
#stream = yt.streams.filter(only_audio=True).first()
# downloading a video would be:
stream = yt.streams.first() 

# download into working directory
stream.download()
