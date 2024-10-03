#!/usr/bin/python3

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, url_for, session, request, redirect, render_template
import json, time, random
import pandas as pd
import api as api
from implems import get_keys



app = Flask(__name__)
TOKEN_INFO = 'token_info'
app.secret_key = ''.join( [str(random.randint(0, 9)) for _ in range(25)] )
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'

@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('get_input',_external=True))

@app.route('/create_list_add')
def create_lst():
    try: 
        token_info = get_token()
    except:
        print('User not logged in')
        return redirect("/")
    sp = spotipy.Spotify(auth=token_info['access_token'])
    print(F:=sp.current_user()['id'])
    ab = sp.user_playlist_create(F, "testCreation", True)

    return ab

@app.route('/authorize')
def authorize():
    sp_oauth = create_spotify_oauth()
    print(sp_oauth)
    session.clear()
    code = request.args.get('code')
    
    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = token_info
    print(token_info)
    return redirect("/input")

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

@app.route('/get_spotify_links/<id>/')
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
        titles = [f['snippet']['title'] for f in list_of_vids]
        try: 
            token_info = get_token()
        except:
            print('User not logged in')
            return redirect("/")
        sp = spotipy.Spotify(auth=token_info['access_token'])
        uris = []
        print(len(titles))
        for title in titles:
            m = sp.search(title, 1)
            uris.append(m['tracks']['items'][0]['uri'])
        user_id = sp.current_user()['id']
        resp = sp.user_playlist_create(user_id, "Test", True)
        playlist_id = resp['id']
        respf = sp.user_playlist_add_tracks(user_id, playlist_id, uris, None)
        return redirect(resp['external_urls']['spotify'])
    return render_template("form.html", ag=titles)

@app.route("/testing/<id>")
def test_id(id):
    return api.get_items_from_youtube_playlist_id(id)



@app.route('/get_spotify_playlists', methods =["GET"])
def get_spots():
    return api.get_items_from_playlist_id("4BECQZKtg5DQGbT9wM17BN")

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login', _external=False))
    
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if(is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = get_keys()['client_id'],
        client_secret = get_keys()['client_secret'],
        redirect_uri = url_for('redirect_page', _external=True),
        scope='user-library-read playlist-modify-public playlist-modify-private'
    )


if __name__ == "__main__":
  api.get_keys()
  app.run()