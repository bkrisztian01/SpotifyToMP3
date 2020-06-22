from __future__ import unicode_literals
import sys
import youtube_dl

track_ids = []
with open("results_ids_copy.txt") as f:
        for i, l in enumerate(f):
            track_ids.append(l.strip())
 

for i in range(len(track_ids)):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'songs/' + str(i + 1) + ' - %(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([track_ids[i]])

