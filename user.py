import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

print("\033c", end='')

cli_id="8549e05651e64b68b52fe6cd6de1b1b2"    
# cli_id = os.environ.get('client_id')
cli_secret="5bdb61996db743548853462ea162bb4a"
# cli_secret = os.environ.get('client_secret')
kill = False

if not cli_secret:
    print("[ERROR] Unable to retrieve Client Secret")
    kill = True
if not cli_id:
    print("[ERROR] Unable to retrieve Client ID")
    kill = True

if kill: exit()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cli_id,
                                               client_secret=cli_secret,
                                               redirect_uri="http://localhost:8888/",
                                               scope="user-library-read"))


results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))

class User:
    def __init__():
        