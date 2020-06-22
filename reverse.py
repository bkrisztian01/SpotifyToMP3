import json

import spotipy
import spotipy.util as util

from youtube_search import YoutubeSearch

credentials = json.load(open('credentials.json'))
track_list = []

playlist_link = "spotify:playlist:3xt67f6tY5Tj4PaLIVUSdv"

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

with open("asd.txt", "w") as f:
    f.write(json.dumps(sp.playlist(playlist_link, fields = "tracks.total, tracks.items.track.artists.name, tracks.items.track.name")))