
from dataclasses import dataclass
@dataclass
class Keys:
    key: str = ""
    client_id: str = ""
    client_secret: str = ""

default_keys = Keys()
spotify_search_data = {
    'grant_type': 'client_credentials',
    'client_id': default_keys.client_id,
    'client_secret': default_keys.client_secret,
}

def get_keys():
    f = open("secret_keys.txt", "r")
    default_keys = Keys(*f.read().split())
    global spotify_search_data
    spotify_search_data = {
        'grant_type': 'client_credentials',
        'client_id': default_keys.client_id,
        'client_secret': default_keys.client_secret,
}
