import os
import json

import spotipy
import spotipy.util as util

from youtube_search import YoutubeSearch
import youtube_dl

credentials = json.load(open('credentials.json'))
track_list = []

# playlist_link = input("Paste in your playlist link: ")
playlist_link = 'spotify:playlist:3xt67f6tY5Tj4PaLIVUSdv'

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

tracks = sp.playlist(playlist_link, fields = "tracks.total, tracks.items.track.artists.name, tracks.items.track.name")['tracks']

track_youtube_ids = []

for i in range(len(tracks['items'])):
    print(len(tracks['items']))
    songname = ''
    for j in tracks['items'][i]['track']['artists']:
        songname = songname + j['name'] + ' '
    songname = songname + tracks['items'][i]['track']['name']
    print(songname)
    # results = []
    # while(len(results) == 0):
    #     results = YoutubeSearch(songname, max_results = 1).to_dict()
    # track_youtube_ids.append(results[0]['id'])

