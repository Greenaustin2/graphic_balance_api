from googleapiclient.discovery import build
import random
# import urllib.request
# import re
from pprint import pprint
import webbrowser
from pytube import YouTube
from pytube import Channel

from yt import Search
from yt import Files
from yt import Playlists
from yt import current_time

files = Files()
search = Search()
playlists = Playlists()
date = current_time()
# [-----------------------------------------------------------------------------------------------------]
# ~search~search~search~search~search~search~search~search~search~search~search~search~search~search~search~
# Search Criteria:
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
search.video_definition = 'high'
search.video_duration = 'any'
search.title_chars = 18
search.embed = 'any'
search.type = 'video'
search.video_limit = 100
search.output_path = '/Volumes/graphic_balance/01_25_23'
search.order = 'relevance'
search.file_size = 2e8
search.random = 'yes'
# search.formats = 'img'
# search.query = 'video'
search.published_before = current_time()
search.published_after = '2005-04-23T00:00:00Z'
# api.location =
# api.location_radius =


# search.download()
# search.stream()

# [--------------------------------------------------------------------------------------------------]
# ~files~files~files~files~files~files~files~files~files~files~files~files~files~files~files~files~files
# Origin Directory // path to files whose channels intend to be downloaded
# Destination Directory // path to directory in which channel folders will be created

files.origin_directory = '/Volumes/graphic_balance/01_22_23/links/'
files.destination_directory = '/Volumes/graphic_balance/01_22_23/channels/'

files.channel_browser()
# files.channel_download()


# [--------------------------------------------------------------------------------------------------]
#~playlist~playlist~playlist~playlist~playlist~playlist~playlist~playlist~playlist~playlist~playlist~

# Destination Directory // location for downloads to be stored

playlists.destination_directory = '/Volumes/graphic_balance/01_21_23/selects/inspect/'
#
# playlists.download('https://www.youtube.com/playlist?list=PLY7pdVS9M2Bbu0ppeifXs9mu5xQootY88')






















