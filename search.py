import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# Load credentials
try:
    with open("creds.json", "r") as file:
        data = json.load(file)
        client_id = data['clientId']
        client_secret = data['clientSecret']
except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
    raise Exception(f"Error loading credentials: {e}")

# Authenticate with Spotify API
sp = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
)

def Search(query: str) -> dict:
    """
    Search for a single track on Spotify.

    :param query: Song name or keywords.
    :return: Dictionary with track details (name, album, artist, image).
    """
    try:
        results = sp.search(query, limit=1)['tracks']['items']
        if not results:
            return {"error": "No results found"}

        track = results[0]
        return {
            'name': track['name'],
            'album': track['album']['name'],
            'artist': track['artists'][0]['name'],
            'image': track['album']['images'][0]['url']
        }
    except Exception as e:
        return {"error": f"Search failed: {e}"}

def SearchAll(query: str, limit: int = 20) -> list:
    """
    Search for multiple tracks on Spotify.

    :param query: Song name or keywords.
    :param limit: Number of results to return (default 5).
    :return: List of dictionaries with track details.
    """
    try:
        results = sp.search(query, limit=limit)['tracks']['items']
        if not results:
            return []

        return [
            {
                'name': track['name'],
                'album': track['album']['name'],
                'artist': track['artists'][0]['name'],
                'image': track['album']['images'][0]['url']
            }
            for track in results
        ]
    except Exception as e:
        return {"error": f"Search failed: {e}"}

