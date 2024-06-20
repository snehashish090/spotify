import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import eyed3
from eyed3.id3.frames import ImageFrame
from pytube import YouTube
from moviepy.editor import *
import os
from pytube import Search
import search
import sys
import json
from pathlib import Path

export_path = str(Path(__file__).parent)+"/exports/"

if not os.path.exists(export_path):
    os.mkdir(export_path)

if not os.path.exists('config.json'):
    with open('config.json', 'w') as file:   
        json.dump([export_path], file)

if not os.path.exists('creds.json'):
    with open('creds.json', 'w') as file:
        clientId = input("enter client id: ")
        clientSecret = input("enter client secret: ")   
        json.dump({
            "clientId":clientId,
            "clientSecret":clientSecret
        }, file)

if not os.path.exists('images/'):
    os.mkdir('images/')

# Getting Auth details
with open("creds.json","r") as file:
    data = json.load(file)
    clientId=data['clientId']
    clientSecret=data['clientSecret']

# Function to download the image
def pdownload(url, name):
    print("Downloading the Image...")
    req = requests.get(url)
    with open('images/'+name+'.jpg', 'wb') as file:
        file.write(req.content)
    print("Image Download successfull")

# Function to download the song
def Download(link, name, path):
    print("Downloading the Video")
    # Intiaizing the YouTube object
    youtubeObject = YouTube(link)
    # Getting the video
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        # Downloading it
        youtubeObject.download(os.path.join(path), filename=name+'.mp4')
        print("Download Successfull")
    except:
        # Handling Error
        print("An error has occurred")

    print("Converting Video to Audio")

    # Using moviepy to convert mp4 to mp3
    video = VideoFileClip(os.path.join(path,name+".mp4"))
    video.audio.write_audiofile(
        os.path.join(path,name+".mp3"))
    
    # Removing the mp4
    os.remove(os.path.join(path,name+".mp4"))

    print(("Converted to mp3 format Successfully"))

# Function to get the url for a song from YouTube
def searchYoutube(name):
    x = Search(name).results
    if len(x) == 0:
        return 'Not Found'
    else:
        return x[0].watch_url

# Authentication - without user
client_credentials_manager = SpotifyClientCredentials(
    client_id=clientId, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def Single(name:str,artist:str,album:str,ur:str, path:str):
    
    # Getting the YouTube
    url = searchYoutube(name+" "+artist + " Official Original Audio ")

    # Downloading the Cover Art
    pdownload(ur, name)
    
    # Downloading the YouTube video as mp3
    Download(url, name.replace(' ', '-'), path)

    # Editing the metadata
    audiofile = eyed3.load(path+'/'+name.replace(' ', '-')+'.mp3')
    if (audiofile.tag == None):
        audiofile.initTag()
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(
        'images/'+name+'.jpg', 'rb').read(), 'image/jpeg')
    audiofile.tag.artist = artist
    audiofile.tag.title = name
    audiofile.tag.album = album
    audiofile.tag.save()

    os.remove('images/'+name+".jpg")
    print("Done")
    


def Playlist(playlist_link:str, path:str):
    """
    Function to get download a public spotify playlist

    params:
        -playlist_link
        -path
    """
    
    # Fetching the playlist data from the Spotify API
    playlist = sp.playlist_tracks(playlist_link)
    return playlist
    # Getting the length of the playlist
    l = len(playlist['items'])

    # Going through every song in the playlist
    for i in playlist['items']:

        # Getting the details of the song
        name = i['track']['name']
        artist = i['track']['artists'][0]['name']
        album = i['track']['album']['name']
        ur = i['track']['album']['images'][0]['url']

        # Downloading the Album Art for the song
        pdownload(ur, name)
        
        # Getting the YouTube url for a song 
        url = searchYoutube(name+" "+artist + " Audio ")
        
        # Downloading the YouTube video as an mp3
        Download(url, name.replace(' ', '-'), path)

        # Editing the metadata of the file
        audiofile = eyed3.load(path+'/'+name.replace(' ', '-')+'.mp3')
        if (audiofile.tag == None):
            audiofile.initTag()
        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(
            'images/'+name+'.jpg', 'rb').read(), 'image/jpeg')

        audiofile.tag.artist = artist
        audiofile.tag.title = name
        audiofile.tag.album = album
        audiofile.tag.save()

        os.remove('images/'+name+".jpg")


