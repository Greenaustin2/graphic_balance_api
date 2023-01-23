import os
from pytube import YouTube
from pytube import Channel
import webbrowser


file_list = os.listdir('/Volumes/graphic_balance/new/tagged')
print(file_list)

video_id_list = []
for file in file_list:
    if file.endswith(".mp4"):
        file = file[:11]
        video_id_list.append(file)
print(video_id_list)


for video in video_id_list:
    url = "https://www.youtube.com/watch?v=" + video + "/videos"
    print(video)
    x = YouTube(url)
    curl = x.channel_url
    # c = Channel(curl)
    print(curl)
    proceed = input("next?")
    if proceed == 'y':
        print(f"downloading {curl}")
        webbrowser.open_new_tab(curl)