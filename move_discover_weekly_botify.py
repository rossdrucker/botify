# -*- coding: utf-8 -*-
"""
@author: Ross Drucker
"""

from botifunctions import authorize, get_track_ids_from_playlist

discover_weekly_id = '37i9dQZEVXcPgVqvfqWHGE' # Discover Weekly

user_id = 'rossdrucker9'

sp = authorize()

discover_weekly_tracks = get_track_ids_from_playlist(sp, playlist_id = discover_weekly_id)

sp.user_playlist_add_tracks(user_id, '17NCMIxHftu2lNiYav25t0', discover_weekly_tracks)