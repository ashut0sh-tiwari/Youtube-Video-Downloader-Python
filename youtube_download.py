#first install pytube using pip

#import this to download single video
from pytube import YouTube
#import this to download playlist
from pytube import Playlist

#paste your youtube video link in this 
link = "https://www.youtube.com/watch?v=2g2sXGixh3w"

#using youtube function which takes link as an arguement
youtube_1 = YouTube(link)

#function to get youtube video title
print(youtube_1.title)

#function to get youtube video title
# print(youtube_1.thumbnail_url)

#funtion to get all audio streams in which video can be downloaded
# videos = youtube_1.streams.filter(only_audio=True)


#funtion to get all streams in which video can be downloaded
videos = youtube_1.streams.all()
# print(videos)
vid = list(enumerate(videos))


#function to print all stream quality
for i in vid:
    print(i)

#function to get the desired input from the user
strm = int(input("enter : "))

#function to download youtube video
videos[strm].download()



#function to download youtube playlist

py = Playlist("")

print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()

# print("succesfully")

