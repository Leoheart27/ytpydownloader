from pytube import YouTube

yt = YouTube("url of the video here") ## url of the video


print("Title: ", yt.title)
print("Number of views: ", yt.views) ## views of the video
print("Length of video: ", yt.length) ## lenght of the video in seconds
print("Description: ", yt.description) ## description of the video


ys = yt.streams.get_highest_resolution() ## get the video with the highest resolution
ys.download("C:/Users/Username/videos") ## directory where you want to download