from googleapiclient.discovery import build
import os
import urllib.request
import random
from pytube import YouTube
from pytube import Channel
from pytube import Playlist
# from pytube.cli import on_progress
import datetime
import pprint
import webbrowser
import shutil
from tqdm import tqdm
import sys

API_KEY = "AIzaSyBBFpmVkJLy-5iy-4nMGjlzEZWoAfziuuU"
YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)



def current_time():
    utc_now = datetime.datetime.utcnow()
    return utc_now.strftime('%Y-%m-%dT%H:%M:%SZ')
    # utc_now.replace('+00:00', 'Z')


class Search:
    """includes all api functionality"""

    def __init__(self):
        self.formats = ["mp4", "wmv", "avi", "mov", "img", "gopr"]
        self.number = 0
        self.format = ''
        self.max_results = 50
        self.order = 'relevance'
        self.video_def = 'any'
        self.title_chars = 18
        self.embed = 'any'
        self.video_duration = 'any'
        self.type = 'video'
        self.video_limit = 100
        self.output_path = '/Volumes/graphic_balance/'
        self.file_size = 1e8
        self.random = 'yes'
        self.published_before = current_time()
        self.published_after = '2005-04-23T00:00:00Z'
        self.query()
        # self.query()
        # self.location = ''
        # self.location_rad = ''

    def query(self):
        """Outputs 4-digit number formatted with randomly chosen file type from file type list. takes number as input"""
        self.number = str(random.randint(1, 10 ** 4)).zfill(4)
        self.format = random.choice(self.formats)
        if self.format == "gopr":
            return f"{self.format}{self.number}"
        elif self.format == "mov" or self.format == "img":
            return f"{self.format} {self.number}"
        else:
            return f"{self.number}.{self.format}"

    def api_request(self):
        """Conducts search as per search criteria. A list of video ID's are compiled in a list, chosen at random"""
        videos = []
        # API search criteria
        # print(self.query)
        request = YOUTUBE.search().list(
            part='snippet',
            q=self.query(),
            order=self.order,
            type=self.type,
            maxResults=self.max_results,
            videoDefinition=self.video_def,
            videoEmbeddable=self.embed,
            videoDuration=self.video_duration,
            publishedBefore=self.published_before,

            # publishedAfter=self.published_after,
            # location=self.location,
            # locationRadius=self.location_rad,
        )
        response = request.execute()
        files = response["items"]
        loop_is_on = True
        while loop_is_on:
            for v_id in files:
                # title of video as a string
                title = str(v_id["snippet"]["title"]).lower()
                # check if search query is in video title before appending to video ID list
                if self.number and self.format in title:
                    if len(title) <= self.title_chars:
                        videos.append(v_id["id"]["videoId"])
                    else:
                        pass
            if len(videos) > 1:
                loop_is_on = False
            else:
                pass
        return videos
# ADD DOWNLOAD PROGRESS BAR

    def download(self):
        if self.random == 'yes':
            for _ in range(0, self.video_limit):
                video_id = random.choice(self.api_request())
                yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
                vid_info = f"{video_id}_{yt.author}_{yt.channel_id}_{yt.publish_date.date()}_{yt.views}_"
                yt = yt.streams.get_highest_resolution()
                if yt.filesize < self.file_size:
                    print(f"downloading {video_id}")
                    yt.download(output_path=self.output_path, filename_prefix=vid_info)
                    with open("search_history.txt", mode='a') as search:
                        search.write(f"{self.query()}\n")

                    # create list and append each downloaded videos file size and use to calculate total download limit
                else:
                    continue
        elif self.random == 'no':
            video_id = self.api_request()
            print(f"downloading {self.query}...")
            for _ in range(0, self.video_limit):
                yt = YouTube(f"https://www.youtube.com/watch?v={video_id[_]}")
                vid_info = f"{video_id[_]}_{yt.publish_date.date()}_{yt.views}_"
                yt = yt.streams.get_highest_resolution()
                if yt.filesize < self.file_size:
                    yt.download(output_path=self.output_path, filename_prefix=vid_info)
                    with open("search_history.txt", mode='a') as search:
                        search.write(f"{self.query()}\n")

                else:
                    pass

    def stream(self):
        """opens specified number of query results in browser"""
        streaming = True
        while streaming:
            if self.random == 'yes':
                for _ in range(0, self.video_limit):
                    video_id = random.choice(self.api_request())
                    webbrowser.open_new_tab(f"https://www.youtube.com/watch?v={video_id}")
                    with open("search_history.txt", mode='a') as search:
                        search.write(f"{self.query()}\n")
                streaming = False
            elif self.random == 'no':
                video_id = self.api_request()
                print(video_id)
                if self.video_limit <= len(video_id):
                    for vid in range(0, self.video_limit):
                        webbrowser.open_new_tab(f"https://www.youtube.com/watch?v={video_id[vid]}")
                        with open("search_history.txt", mode='a') as search:
                            search.write(f"{self.query()}\n")
                    streaming = False
                else:
                    pass


class Files:
    """processing of locally hosted files"""
    def __init__(self):
        self.origin_directory = '/volumes/graphic_balance/01_22_23'
        self.destination_directory = '/volumes/graphic_balance/01_22_23'

    # def channel_download(self):
    #     """retrieves channel address from single videos in specified folders and downloads contents of channel"""
    #     video_id_list = []
    #     video_file_names = []
    #     file = 0
    #     directory = os.listdir(self.origin_directory)
    #     for file in directory:
    #         if file.endswith(".mp4"):
    #             video_id_list.append(file[:11])
    #             video_file_names.append(file)
    #     for video in video_id_list:
    #         x = YouTube("https://www.youtube.com/watch?v=" + video)
    #         curl = x.channel_url
    #         c = Channel(curl)
    #         # make download directory
    #         directory = c.channel_name
    #         path = os.path.join(self.destination_directory, directory)
    #         os.mkdir(path)
    #         for videos in c.videos:
    #             for ids in c.video_urls:
    #                 vid_id = ids[-11:]
    #                 yt = YouTube(ids)
    #                 vid_info = f"{vid_id}_{yt.publish_date.date()}_{yt.views}_"
    #                 print(f"downloading {vid_info}")
    #                 videos.streams.get_highest_resolution().download(output_path=path, filename_prefix=vid_info)
    #         # for file in video_file_names:
    #         #     shutil.move(self.origin_directory + file, path)

    def channel_download(self):
        video_id_list = []
        directory = os.listdir(self.origin_directory)
        for file in directory:
            if file.endswith(".mp4"):
                video_id = file[:11]
                x = YouTube("https://www.youtube.com/watch?v=" + video_id)
                curl = x.channel_url
                c = Channel(curl)
                path = os.path.join(self.destination_directory, c.channel_name)
                os.mkdir(path)
                for videos in c.video_urls:
                    try:
                        yt = YouTube(videos)
                        vid_info = f"{yt.video_id}_{yt.publish_date.date()}_{yt.views}_"
                        print(f"downloading {vid_info}")
                        yt.streams.get_highest_resolution().download(output_path=path, filename_prefix=vid_info)
                    except:
                        pass
                shutil.move(self.origin_directory + file, path)

    def channel_browser(self):
        directory = os.listdir(self.origin_directory)
        print(len(directory))
        if len(directory) > 10:
            for file in directory:
                if file.endswith('.mp4'):
                    video_id = file[:11]
                    link = "https://www.youtube.com/watch?v=" + video_id
                    print(link)

        else:
            for file in directory:
                if file.endswith('.mp4'):
                    video_id = file[:11]
                    link = "https://www.youtube.com/watch?v=" + video_id
                    x = YouTube(link)
                    curl = x.channel_url
                    webbrowser.open_new_tab(curl)


class Playlists:
    """retrieves items from playlists"""
    def __init__(self):
        self.destination_directory = '/volumes/graphic_balance/01_22_23/random_playlist'

    def download(self, url):
        """downloads playlist from playlist url"""
        p = Playlist(url)
        x = 0
        for videos in p.videos:
            url = p.video_urls[x]
            vid_id = url[-11:]
            yt = YouTube(url)
            x += 1
            vid_info = f"{vid_id}_{yt.author}_{yt.channel_id}_{yt.publish_date.date()}_{yt.views}_"
            print(f"downloading {vid_info}...")
            videos.streams.get_highest_resolution().download(output_path=self.destination_directory, filename_prefix=vid_info)





