from flask import Flask, redirect, request, render_template, session, url_for
from flask_session import Session
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import modules.sp_info_access as info

app = Flask(__name__)

# Flask-Session configuration
app.config['SESSION_TYPE'] = 'filesystem' # Can also be "redis", "memcached", "mongodb", etc.
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

client_id = os.environ.get("SPOTIPY_CLIENT_ID")   
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")

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
        return render_template('index.html')

@app.route("/top_artists_tracks")
def top_artists_tracks():
    if not session.get('token_info'):
        return redirect("/")
    else:
        token_info = session.get('token_info')
        sp = spotipy.Spotify(token_info['access_token'])

        long_ar = sp.current_user_top_artists(time_range='long_term', limit=25)['items']
        med_ar = sp.current_user_top_artists(time_range='medium_term', limit=25)['items']
        short_ar = sp.current_user_top_artists(time_range='short_term', limit=25)['items']

        long_so = sp.current_user_top_tracks(time_range='long_term', limit=25)['items']
        med_so = sp.current_user_top_tracks(time_range='medium_term', limit=25)['items']
        short_so = sp.current_user_top_tracks(time_range='short_term', limit=25)['items']

        return render_template('top_artists_tracks.html', long_ar=long_ar, med_ar=med_ar, short_ar=short_ar,
                                                long_so=long_so, med_so=med_so, short_so=short_so)
    

@app.route('/genres')
def genres():
    if not session.get('token_info'):
        return redirect("/")
    else:
        token_info = session.get('token_info')
        sp = spotipy.Spotify(token_info['access_token'])

        genres_l = info.MyTopGenres(sp.current_user_top_tracks(time_range='long_term', limit=25)['items'])
        genres_m = info.MyTopGenres(sp.current_user_top_tracks(time_range='medium_term', limit=25)['items'])
        genres_s = info.MyTopGenres(sp.current_user_top_tracks(time_range='short_term', limit=25)['items'])

        return render_template('genres.html',genres_l=genres_l, genres_m=genres_m, genres_s=genres_s)


@app.route('/signout')
def signout():
    # Invalidate the user's session
    session.clear()
    # Redirect the user to the main page (or a sign-in page)
    return redirect(url_for('index'))


@app.route("/callback")
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=port)