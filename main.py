import os
import json
import sys
import progressbar

import spotipy
import spotipy.util as util

from youtube_search import YoutubeSearch
import youtube_dl

credentials = json.load(open('credentials.json'))

playlist_id = input("Paste in your playlist link: ")

username = "11135169461"
scope = ""
SPOTIFY_CLIENT_ID = credentials['Spotify']['client_id']
SPOTIFY_CLIENT_SECRET = credentials['Spotify']['client_secret']
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback/"
token = util.prompt_for_user_token(username,
                           scope,
                           client_id = SPOTIFY_CLIENT_ID,
                           client_secret = SPOTIFY_CLIENT_SECRET,
                           redirect_uri = SPOTIFY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)
offset = 0
track_list = []

while True:
    response = sp.playlist_tracks(playlist_id, offset = offset, fields = "items.track.artists.name, items.track.name")

    if (len(response["items"]) == 0):
        break

    offset += len(response["items"])
    for item in response["items"]:
        track = ""
        for artist in item["track"]["artists"]:
            track = track + artist["name"] + " "
        track = track + item["track"]["name"]
        track_list.append(track)

track_youtube_ids = []
print("---------------------------------")
print("Searching YouTube for video ids:")
for i in progressbar.progressbar(range(len(track_list))):
    results = []
    while(len(results) == 0):
        results = YoutubeSearch(track_list[i], max_results = 1).to_dict()
    track_youtube_ids.append(results[0]['id'])


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
for i in progressbar.progressbar(range(len(track_youtube_ids))):
    ydl_opts["outtmpl"] = 'songs/' + str(i + 1) + ' - %(title)s.%(ext)s'
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([track_youtube_ids[i]])