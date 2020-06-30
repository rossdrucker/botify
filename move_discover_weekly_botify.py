# -*- coding: utf-8 -*-
"""
@author: Ross Drucker
"""

from botifunctions import authorize, get_track_ids_from_playlist, add_tracks_to_playlist

try:
    from botify_settings import username
except:
    username = input('Spotify Username: ')
    with open('botify_settings.py', 'a') as f:
        f.write(f"username = '{username}'")
        f.close()

try:
    from botify_settings import discover_weekly_id
except:
    discover_weekly_id = input('Discover Weekly playlist ID: ')
    with open('botify_settings.py', 'a') as f:
        f.write(f"discover_weekly_id = '{discover_weekly_id}'")
        f.close()

try:
    from botify_settings import discover_weeklies_id
except:
    discover_weeklies_id = input('Discover Weeklies playlist ID: ')
    with open('botify_settings.py', 'a') as f:
        f.write(f"discover_weeklies_id = '{discover_weeklies_id}'")
        f.close()
        
sp = authorize()

discover_weekly_tracks = get_track_ids_from_playlist(sp, playlist_id = discover_weekly_id)

add_tracks_to_playlist(sp, discover_weekly_tracks, discover_weeklies_id)

print(f'Added {len(discover_weekly_tracks)} to Discover Weeklies')