from flask import Flask, redirect, request, render_template, session
from flask_session import Session
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

# Flask-Session configuration
app.config['SESSION_TYPE'] = 'filesystem' # Can also be "redis", "memcached", "mongodb", etc.
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

# client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_id = "8549e05651e64b68b52fe6cd6de1b1b2"    
# client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
client_secret = "5bdb61996db743548853462ea162bb4a"

os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080/callback"
redirect_uri = os.environ.get("SPOTIPY_REDIRECT_URI")

# Extract the port number from the SPOTIPY_REDIRECT_URI
port_from_uri = os.environ.get("SPOTIPY_REDIRECT_URI", "http://localhost:8080").split(":")[-1]
port = int(port_from_uri.split('/')[0])

scope = "user-top-read"
sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)


@app.route("/")
def index():
    if not session.get('token_info'):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    else:
        token_info = session.get('token_info')
        sp = spotipy.Spotify(token_info['access_token'])
        long = sp.current_user_top_artists(time_range='long_term', limit=10)['items']
        med = sp.current_user_top_artists(time_range='medium_term', limit=10)['items']
        short = sp.current_user_top_artists(time_range='short_term', limit=10)['items']
        # for i, artist in enumerate(results):
        #     print(str(i) + " " + artist['name'])

        return render_template('top_artists.html', long=long, med = med, short = short)


@app.route("/callback")
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=port)