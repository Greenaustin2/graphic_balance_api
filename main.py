from googleapiclient.discovery import build
import random
# import urllib.request
# import re
from pprint import pprint
import webbrowser
from pytube import YouTube

api_key = "AIzaSyBMOq2KUZg7xFc29bGF9VKQgRHYMEX7tpQ"
youtube = build('youtube', 'v3', developerKey=api_key)


def number():
    """generates and returns a random number between 0001 and 9999"""
    generated_number = str(random.randint(1, 10 ** 4))
    return generated_number.zfill(4)


def query(number_input, format_choice):
    """Outputs 4-digit number formatted with randomly chosen file type from file type list. takes number as input"""
    if format_choice == "gopr":
        return f"{format_choice}{number_input}"
    elif format_choice == formats[0] or format_choice == formats[1] or format_choice == formats[2] or format_choice == \
            formats[3]:
        return f"{number_input}.{format_choice}"
    else:
        return f"{format_choice}+{number_input}"


def api_request(search):
    """Conducts search as per search criteria. A list of video ID's are compiled in a list, chosen at random"""
    videos = []
    # API request criteria
    request = youtube.search().list(
        part='snippet',
        q=search,
        # Choose order: date, rating, viewCount, relevance, title, videoCount
        order='date',
        type='video',
        # videoDuration="",
        maxResults=50,
        # videoEmbeddable="true"
        # videoDuration=""
        # videoDefenition=""
        # publishedBefore=""
        # publishedAfter=""

    )
    response = request.execute()
    files = response["items"]
    # pprint(files)
    loop_is_on = True
    while loop_is_on:
        for v_id in files:
            # title of video as a string
            title = str(v_id["snippet"]["title"]).lower()
            # check if search query is in video title before appending to video ID list
            if num and format_choice in title:
                if len(title) <= 18:
                    videos.append(v_id["id"]["videoId"])
                else:
                    pass
        if len(videos) > 1:
            loop_is_on = False
        else:
            pass
    video_choice = random.choice(videos)
    return video_choice


for _ in range (0, 100):
    formats = ["mp4", "wmv", "avi", "mov", "img", "gopr"]
    num = number()
    format_choice = random.choice(formats)
    search_query = query(num, format_choice)
    print(search_query)
    video_id = api_request(search_query)
    yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    yt = yt.streams.get_highest_resolution()
    file_size = yt.filesize
    print(file_size)
    video_name = yt.title
    if file_size < 1e8:
        yt.download(output_path='~/Desktop', filename_prefix=f"{video_id}___")
        # filename = yt.title + "/" + video_id,
    else:
        pass





# opens search query and random video separately
# webbrowser.open_new_tab(f"https://www.youtube.com/watch?v={video_id}")
# webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={search_query}")
