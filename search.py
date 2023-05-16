import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

with open("creds.json","r") as file:
    data = json.load(file)
    clientId=data['clientId']
    clientSecret=data['clientSecret']

# Authentication - without user
client_credentials_manager = SpotifyClientCredentials(
    client_id=clientId, client_secret=clientSecret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to search and get only one result
def Search(name):
    var = sp.search(name)['tracks']['items'][0]

    return {
        'name': var['name'],
        'album': var['album']['name'],
        'artist': var['album']['artists'][0]['name'],
        'image': var['album']['images'][0]['url'],
        'var': var
    }

# Function to get all the results for a search query
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

