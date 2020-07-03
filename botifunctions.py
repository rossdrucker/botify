# -*- coding: utf-8 -*-
"""
@author: Ross Drucker
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authorize(scope = 'playlist-modify-public'):
    try:
        from botify_settings import client_id, client_secret, redirect_uri, username
        auth_manager = SpotifyOAuth(
            client_id = client_id,
            client_secret = client_secret,
            redirect_uri = redirect_uri,
            username = username,
            scope = scope
        )
        
        sp = spotipy.Spotify(auth_manager = auth_manager)
        return sp
    
    except:
        client_id = input('Client ID: ')
        client_secret = input('Client secret: ')
        username = input('Spotify username: ')
        auth_manager = SpotifyOAuth(
            client_id = client_id,
            client_secret = client_secret,
            redirect_uri = 'http://localhost:8888/callback/',
            username = username,
            scope = scope
        )
        sp = spotipy.Spotify(auth_manager=auth_manager)
        
        with open('botify_settings.py', 'w') as f:
            f.write(f"client_id = '{client_id}'\n")
            f.write(f"client_secret = '{client_secret}'\n")
            f.write(f"redirect_uri = 'http://localhost:8888/callback/'\n")
            f.write(f"username = '{username}'")
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

def add_tracks_to_playlist(sp, tracks_to_add, playlist_id, username):
    try:
        sp.user_playlist_add_tracks(username, playlist_id, tracks_to_add)
        return 1
    except:
        return 0