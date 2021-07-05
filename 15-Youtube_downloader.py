#we use the Pytube library for easily download from youtube
from pytube import YouTube


#in this part user can add a url for download video from youtube
yt = YouTube(input("please enter your url:\t"))

try:
    yt.streams.filter(progressive=True , file_extension='mp4').order_by('resolution').desc().first().download()
except:
    print("connection Error")