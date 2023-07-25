import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="8549e05651e64b68b52fe6cd6de1b1b2",
                                               client_secret="5bdb61996db743548853462ea162bb4a",
                                               redirect_uri="YOUR_APP_REDIRECT_URI",
                                               scope="user-library-read"))

