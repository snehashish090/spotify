import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


clientId = "17afd740ee4a41ea9e6c79605a4a2a37"
clientSecret = "264e23c7d072426b89b4182edc0a524e"

# Authentication - without user
client_credentials_manager = SpotifyClientCredentials(
    client_id=clientId, client_secret=clientSecret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def Search(name):
    var = sp.search(name)['tracks']['items'][0]

    return {
        'name': var['name'],
        'album': var['album']['name'],
        'artist': var['album']['artists'][0]['name'],
        'image': var['album']['images'][0]['url'],
        'var': var
    }

def SearchAll(name):
    ans = []
    x = sp.search(name)['tracks']['items']
    for var in x:
        ans.append({
        'name': var['name'],
        'album': var['album']['name'],
        'artist': var['album']['artists'][0]['name'],
        'image': var['album']['images'][0]['url'],
    })
    return ans

