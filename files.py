import os
from pytube import YouTube
from pytube import Channel
from pytube import Playlist


class Files:
    def __init__(self):
        self.origin_directory = '/volumes/graphic_balance/01_22_23'
        self.destination_directory = '/volumes/graphic_balance/01_22_23'

    def channel_download(self):
        video_id_list = []
        directory = os.listdir(self.origin_directory)
        for file in directory:
            if file.endswith(".mp4"):
                video_id_list.append(file[:11])
        for video in video_id_list:
            x = YouTube("https://www.youtube.com/watch?v=" + video)
            curl = x.channel_url
            c = Channel(curl)
            # make download directory
            directory = c.channel_name
            path = os.path.join(self.destination_directory, directory)
            os.mkdir(path)
            for videos in c.videos:
                for ids in c.video_urls:
                    vid_id = ids[-11:]
                    yt = YouTube(ids)
                    vid_info = f"{vid_id}_{yt.publish_date.date()}_{yt.views}_"
                    videos.streams.get_highest_resolution().download(output_path=path, filename_prefix=vid_info)

    # def playlist_download(self, url):
    #     p = Playlist(url)
    #     for videos in p.videos:
    #         for ids in p.video_urls:
    #             vid_id = ids[-11:]
    #             yt = YouTube(ids)
    #             vid_info = f"{vid_id}_{yt.author}_{yt.channel_id}_{yt.publish_date.date()}_{yt.views}_"
    #             videos.streams.get_highest_resolution().download(output_path=self.destination_directory, filename_prefix=vid_info)


class Playlists:
    def __init__(self):
        self.destination_directory = '/volumes/graphic_balance/01_22_23/random_playlist'

    def download(self, url):
        p = Playlist(url)
        x = 0
        for videos in p.videos:
            url = p.video_urls[x]
            vid_id = url[-11:]
            yt = YouTube(url)
            x += 1
            vid_info = f"{vid_id}_{yt.author}_{yt.channel_id}_{yt.publish_date.date()}_{yt.views}_"
            videos.streams.get_highest_resolution().download(output_path=self.destination_directory, filename_prefix=vid_info)








# url = ''
# c = Channel(url)




