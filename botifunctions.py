# -*- coding: utf-8 -*-
"""
@author: Ross Drucker
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def authorize():
    try:
        from botify_settings import client_id, client_secret
        auth_manager = SpotifyClientCredentials(
            client_id = client_id,
            client_secret = client_secret
        )
        sp = spotipy.Spotify(auth_manager = auth_manager, scope = scope)
        return sp
    
    except:
        client_id = input('Client ID: ')
        client_secret = input('Client secret: ')
        auth_manager = SpotifyClientCredentials(
            client_id = client_id,
            client_secret = client_secret
        )
        sp = spotipy.Spotify(auth_manager=auth_manager)
        
        with open('botify_settings.py', 'w') as f:
            f.write(f"""client_id = '{client_id}'
client_secret = '{client_secret}
redirect_uri = 'http://localhost:8888/callback/'
""")
            f.close()
        return sp

def get_track_ids_from_playlist(sp, playlist_id = ''):
    if playlist_id == '':
        playlist_id = input('Playlist ID: ')
        
    if playlist_id[:17] != 'spotify:playlist:':
        playlist_id = 'spotify:playlist:' + playlist_id
    
    offset = 0    
    
    try:
        playlist = sp.playlist_tracks(
            playlist_id,
            offset = offset,
            fields = 'items.track.id, total'
        )
        
    except NameError:
        sp = authorize()
        playlist = sp.playlist_tracks(
            playlist_id,
            offset = offset,
            fields = 'items.track.id, total'
        )
    
    track_ids = []
    
    for song in playlist['items']:
        track_ids.append(song['track']['id'])
    
    if len(track_ids) == 0:
        print('No tracks on this playlist.')
    return track_ids