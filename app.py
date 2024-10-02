#!/usr/bin/python3

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, url_for, session, request, redirect, render_template
import json, time, random
import pandas as pd
import api as api



# TEST_SPOTIFY_PLAYLIST_ID = "0jI3WN8zFZTKraTjJzI2KH"
# App config
app = Flask(__name__)

app.secret_key = ''.join( [str(random.randint(0, 9)) for _ in range(25)] )
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'

@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    print("auth url : - - >",auth_url)
    return redirect(auth_url)

@app.route('/authorize')
def authorize():
    sp_oauth = create_spotify_oauth()
    print(sp_oauth)
    session.clear()
    code = request.args.get('code')
    
    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = token_info
    return redirect("/input")

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

@app.route('/get_spotify/<id>/')
def get_spotify(id):
    PAGE_STRING = ""
    print("id : : - >", id)
    data_tuple = api.get_compiled_song_name_artist_link(id)
    print(data_tuple)
    for song, name, artist, link in data_tuple:
        j = f'<p><strong>{name} - </strong><em>{artist} - <a href="{link}">Spotify Link</a></em></p>\n'
        PAGE_STRING +=  j
    return '<p>{}</p>'.format(PAGE_STRING)

@app.route('/input', methods =["GET", "POST"])
def get_input():
    titles=[]
    if request.method == "POST":
       input = request.form.get("plink")
       list_of_vids = api.get_items_from_youtube_playlist_id(input)
    #    print(list_of_vids[0]['snippet'])
       titles = [f['snippet']['title'] for f in list_of_vids]
    return render_template("form.html", ag=titles)

# Checks to see if token is valid and gets a new token if not
def get_token():
    token_valid = False
    token_info = session.get("token_info", {})

    # Checking if the session already has a token stored
    if not (session.get('token_info', False)):
        token_valid = False
        return token_info, token_valid

    # Checking if token has expired
    now = int(time.time())
    is_token_expired = session.get('token_info').get('expires_at') - now < 60

    # Refreshing token if it has expired
    if (is_token_expired):
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))

    token_valid = True
    return token_info, token_valid


def create_spotify_oauth():
    return SpotifyOAuth(
            client_id=api.spotify_search_data['client_id'],
            client_secret=api.spotify_search_data['client_secret'],
            redirect_uri=url_for('authorize', _external=True),
            scope="playlist-modify-public")

if __name__ == "__main__":
  api.get_keys()
  app.run()
