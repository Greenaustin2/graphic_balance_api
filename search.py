from googleapiclient.discovery import build
import urllib.request
import random
from pytube import YouTube
from pytube.cli import on_progress
import datetime
import pprint
import webbrowser

API_KEY = "AIzaSyBMOq2KUZg7xFc29bGF9VKQgRHYMEX7tpQ"
YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)


class Search:

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
        # self.api_request()
        # self.query()
        # self.query()
        # self.published_before = d.isoformat('T' + 'Z')
        # self.published_after = '2005-04-23T00:00:00.000000+00:00Z'
        # self.location = ''
        # self.location_rad = ''

    def query(self):
        """Outputs 4-digit number formatted with randomly chosen file type from file type list. takes number as input"""
        self.number = str(random.randint(1, 10 ** 4)).zfill(4)
        self.format = random.choice(self.formats)
        if self.format == "gopr":
            return f"{self.format}{self.number}"
        elif self.format == "mov":
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
            # publishedBefore=self.published_before,
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
                yt = YouTube(f"https://www.youtube.com/watch?v={video_id}", on_progress_callback=on_progress)
                vid_info = f"{video_id}_{yt.author}_{yt.channel_id}_{yt.publish_date.date()}_{yt.views}_"
                yt = yt.streams.get_highest_resolution()
                if yt.filesize < self.file_size:
                    print(f"downloading {video_id}")
                    yt.download(output_path=self.output_path, filename_prefix=vid_info)

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
                    # create list and append each downloaded videos file size and use to calculate total download limit
                else:
                    pass

    def stream(self):
        streaming = True
        while streaming:
            if self.random == 'yes':
                for _ in range(0, self.video_limit):
                    video_id = random.choice(self.api_request())
                    webbrowser.open_new_tab(f"https://www.youtube.com/watch?v={video_id}")
                streaming = False
            elif self.random == 'no':
                video_id = self.api_request()
                print(video_id)
                if self.video_limit <= len(video_id):
                    for vid in range(0, self.video_limit):
                        webbrowser.open_new_tab(f"https://www.youtube.com/watch?v={video_id[vid]}")
                    streaming = False
                else:
                    pass





# class Download:
#     def __init__(self):
#
#
#     def channel(self):
#






# opens search query and random video separately
# webbrowser.open_new_tab(f"https://www.youtube.com/watch?v={video_id}")
# webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={search_query}")






# In streams.py change line:60 from:
#
# self.bitrate: Optional[int] = stream["bitrate"]
#
# to:
#
# try:
#     self.bitrate: Optional[int] = stream["bitrate"]
# except KeyError:
#     print("Key Error: bitrate assigned 30")
#     self.bitrate = 30

