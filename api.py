import requests, json
key = "AIzaSyDtrY2uNWkMEvl5pom7hjjbnVfa8EQDSoE"

def info_from_id(i):
    # print(i['id'])
    if i['id']['kind'] != 'youtube#video':
        return
    vid_id = i['id']['videoId']
    response = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={vid_id}&key={key}")
    rdict = response.json()['items']
    # json_object = json.dumps(rdict, indent=4)
    # print(json_object)
    print(rdict[0]['snippet']['title'])
    print("------------------------------------------------------------------------------------------------")

def get_items_from_youtube_playlist_id(id):
    print("get_items_from_youtube_playlist_id id -> ", id)
    limit = 10
    response = requests.get(f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={limit}&playlistId={id}&key={key}")
    return response.json()['items']
# its = get_items_from_playlist_id("PLlc94szfcNDF8iufUTmqxHBnms5XkoUFR")

def get_titles_from_youtube_playlist(id: str) -> list[str]:
    print("id   ->" , id)
    items = get_items_from_youtube_playlist_id(id)
    return [i['snippet']['title'] for i in items]

# print(*get_titles_from_playlist("PLxRoKEitVdeog3fXfl7KQit3CTSVvpHrG"), sep = "\n")


spotify_search_data = {
    'grant_type': 'client_credentials',
    'client_id': '367f62522e71473bb56f804debd1b85e',
    'client_secret': '5957e304aba146f286d1c879d7e06cc6',
}

def get_spotify_token():

    response = requests.post('https://accounts.spotify.com/api/token', data = spotify_search_data)
    return response.json()['access_token']

spotify_endpoint = "https://api.spotify.com/v1/search"

#response = requests.get(spotify_endpoint + "?q=nine inch nails" + f"&access_token={get_spotify_token()}&token_type=Bearer")
spotify_token = ["DUMMY2oken"]

def search_for_song_on_spotify(q):
    headers = {
        'Authorization': f'Bearer {spotify_token[0]}'}
    params = {
        'q': f"{q}",
        'type': 'track',
        'limit' : 1,
    }
    test_response = requests.get(f'https://api.spotify.com/v1/search', headers=headers, params=params)
    if test_response.status_code == 401:
        spotify_token[0] = get_spotify_token()
        # print(spotify_token)
        return search_for_song_on_spotify(q)
    response = requests.get(f'https://api.spotify.com/v1/search', params=params, headers=headers)
    return response.json()['tracks']["items"][0]


def get_name_url_spotify_link(q:str):
    f = search_for_song_on_spotify(q)
    return (f['name'], f['artists'][0]['name'], f['external_urls']['spotify'])

def get_my_id():
    headers = {
        'Authorization': f'Bearer {spotify_token[0]}',}
    test_response = requests.get('https://api.spotify.com/v1/me', headers=headers)
    if test_response.status_code == 401:
        spotify_token[0] = get_spotify_token()
        # print(spotify_token)
        get_my_id()

def get_compiled_song_name_artist_link(yt_playlistID:str) -> list[tuple]:
    res = []
    for song in get_titles_from_youtube_playlist(yt_playlistID):
        name, artist, link = get_name_url_spotify_link(song)
        f = (song, name, artist, link)
        res.append(f)
    return res

def get_items_from_playlist(id: str):
    headers = {
        'Authorization': f'Bearer {spotify_token[0]}'}
    params = {
        'q': "a",
        'type': 'track',
        'limit': 5,
    }
    test_response = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)
    # print(spotify_token[0], test_response.json())
    if test_response.status_code == 401:
        spotify_token[0] = get_spotify_token()
        return get_items_from_playlist(id)
    
    response = requests.get(f'https://api.spotify.com/v1/playlists/{id}', headers=headers)
    json_object = json.dumps(response.json(), indent=4)
    return json_object

def get_items_from_playlist_id(id: str):
    headers = {
        'Authorization': f'Bearer {spotify_token[0]}'}
    params = {
        'q': "a",
        'type': 'track',
        'limit': 1,
    }
    test_response = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)
    # print(spotify_token[0], test_response.json())
    if test_response.status_code == 401:
        spotify_token[0] = get_spotify_token()
        return get_items_from_playlist(id)
    params = {
        'limit' : 1,
    }
    
    response = requests.get(f'https://api.spotify.com/v1/playlists/{id}/tracks', params=params, headers=headers)
    json_object = json.dumps(response.json()['items'], indent=4)
    
    return json_object

def post_song_to_playlist_id(id: str):
    headers = {
        'Authorization': f'Bearer {spotify_token[0]}'}
    params = {
        'q': "a",
        'type': 'track',
        'limit': 1,
    }
    test_response = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)
    # print(spotify_token[0], test_response.json())
    if test_response.status_code == 401:
        spotify_token[0] = get_spotify_token()
        return get_items_from_playlist(id)
    headers = {
    'Authorization': f'Bearer {spotify_token[0]}',
    'Content-Type': 'application/json',
    }

    json_data = {
        'uris': [
            'spotify:track:4iV5W9uYEdYUVa79Axb7Rh',
        ],
        'position': 0,
    }

    response = requests.post(f'https://api.spotify.com/v1/playlists/{id}/tracks', headers=headers, json=json_data)
    json_object = json.dumps(response.json(), indent=2)
    return json_object

def authenticate():
    redirect_uri = 'http://127.0.0.1:5000/get_spotify/'
    url = 'https://accounts.spotify.com/authorize'
    url += f'?response_type=token&client_id={spotify_search_data["client_id"]}&scope=playlist-modify-public&redirect_uri={redirect_uri}'

    response = requests.get(url)
    
    # json_object = json.dumps(response.json(), indent = 2)
    # return json_object


def main():
    spotify_token[0] = get_spotify_token()
    print(get_compiled_song_name_artist_link("PLxRoKEitVdeqU_i2ygY7jrgPlO8HLNwK9"))

if __name__ == "__main__":
    main()