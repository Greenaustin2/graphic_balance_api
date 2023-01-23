from googleapiclient.discovery import build
import random
# import urllib.request
# import re
from pprint import pprint
import webbrowser
from pytube import YouTube
from pytube import Channel

from search import Search
from files import Files
from files import Playlists

files = Files()
search = Search()
playlists = Playlists()
# [-----------------------------------------------------------------------------------------------------]
# Order // relevance, date, rating, title, viewCount
# Max Results // query results returned, any int. default value 50
# Video Definition // any, high, standard
# Video Duration // any, long (> 20 min), medium (> 4, < 20 min), short (< 4 min)
# Title Characters // input integer, auto 18
# Video Embed // any, true
# Type // channel, playlist, video
# Published Before // RFC 3339 time format (1970-01-01T00:00:00Z)
# Published After // RFC 3339 time format (1970-01-01T00:00:00Z)
# Location // used in conjunction with location_rad, string defines long and lat coordinates(37.42307,-122.08427)
# Location Radius // used in conjunction with location, value must be float w/ unit (m, km, ft, mi)
# Download Limit // number of videos to be downloaded at random, int
# Output Path // file path to download location
# File Size // maximum file size, int value in bytes. default value 1e8
# Random // 'yes' will download one video per query, while 'no' will download videos from a single query
# Stream // will open videos from search query, takes 1 positional argument of int for number of results

search.max_results = 50
search.video_definition = 'any'
search.video_duration = 'any'
search.title_chars = 18
search.embed = 'any'
search.type = 'video'
search.video_limit = 300
search.output_path = '/Volumes/graphic_balance/01_22_23'
search.order = 'relevance'
search.file_size = 1e8
search.random = 'yes'
# search.formats = 'img'
# api.published_before = d.isoformat('T')
# api.published_after = '2005-04-23T00:00:00.000000+00:00Z'
# api.location =
# api.location_radius =


# search.download()

# Origin Directory // path to files whose channels intend to be downloaded
# Destination Directory // path to directory in which channel folders will be created

# files.origin_directory = '/volumes/graphic_balance/01_22_23'
# files.destination_directory = '/volumes/graphic_balance/01_22_23'
# files.channel_download()



#
# Destination Directory // location for downloads to be stored
playlists.destination_directory = '/volumes/graphic_balance/01_22_23/random_playlist'
playlists.download('https://www.youtube.com/playlist?list=PLY7pdVS9M2BYWAV0r9-2T5yScHskJEdc6')



























# def number():
#     """generates and returns a random number between 0001 and 9999"""
#     generated_number = str(random.randint(1, 10 ** 4))
#     return generated_number.zfill(4)
#
#
# def query(number_input, format_option):
#     """Outputs 4-digit number formatted with randomly chosen file type from file type list. takes number as input"""
#     if format_option == "gopr":
#         return f"{format_option}{number_input}"
#     elif format_option == formats[0] or format_option == formats[1] or format_option == formats[2] or format_option == \
#             formats[3]:
#         return f"{number_input}.{format_option}"
#     else:
#         return f"{format_option} {number_input}"
#
#
# def api_request(search):
#     """Conducts search as per search criteria. A list of video ID's are compiled in a list, chosen at random"""
#     videos = []
#     # API request criteria
#     request = youtube.search().list(
#         part='snippet',
#         q=search,
#         # Choose order: date, rating, viewCount, relevance, title, videoCount
#         order='relevance',
#         type='video',
#         # videoDuration="",
#         maxResults=50,
#         # videoEmbeddable="true"
#         # videoDuration=""
#         videoDefinition="any",
#         # publishedBefore=""
#         # publishedAfter=""
#
#     )
#     response = request.execute()
#     # pprint(response)
#     files = response["items"]
#     loop_is_on = True
#     while loop_is_on:
#         for v_id in files:
#             # title of video as a string
#             title = str(v_id["snippet"]["title"]).lower()
#             # check if search query is in video title before appending to video ID list
#             if num and format_choice in title:
#                 if len(title) <= 18:
#                     videos.append(v_id["id"]["videoId"])
#                 else:
#                     pass
#         if len(videos) > 1:
#             loop_is_on = False
#         else:
#             pass
#     video_choice = random.choice(videos)
#     return video_choice
#
#
# def is_file_size(youtube_file, size_max):
#     if youtube_file < size_max:
#         return True
#     else:
#         return False
#
#
#
# for _ in range(0, 500):
#     formats = ["mp4", "wmv", "avi", "mov", "img", "gopr"]
#     num = number()
#     format_choice = random.choice(formats)
#     search_query = query(num, format_choice)
#     print(search_query)
#     video_id = api_request(search_query)
#     yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
#     vid_info = f"{video_id}_{yt.author}_{yt.channel_id}_{yt.publish_date.date()}_{yt.views}_"
#     #  _ {yt.publish_date.date()} _ {yt.views}
#     yt = yt.streams.get_highest_resolution()
#     if is_file_size(yt.filesize, 1e8):
#         yt.download(output_path='/Volumes/graphic_balance/1_21_22', filename_prefix=vid_info)
#         # create list and append each downloaded videos file size and use to calculate total download limitpython.p
#     else:
#         pass
#     # file_size = yt.filesize
#     # print(file_size)







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

