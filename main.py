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


if not os.path.exists('config.json'):
    with open('config.json', 'w') as file:   
        json.dump([], file)



if not os.path.exists('images/'):
    os.mkdir('images/')

clientId = "17afd740ee4a41ea9e6c79605a4a2a37"
clientSecret = "264e23c7d072426b89b4182edc0a524e"


def pdownload(url, name):
    req = requests.get(url)
    with open('images/'+name+'.jpg', 'wb') as file:
        file.write(req.content)


def Download(link, name, path):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(path, filename=name+'.mp4')
    except:
        print("An error has occurred")

    video = VideoFileClip(path+'/'+name+".mp4")
    video.audio.write_audiofile(
        path+'/'+name+".mp3", verbose=None, logger=None)
    os.remove(path+'/'+name+".mp4")


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
# x = input('enter mode (playlist/single):')


def playlist(path):
    test = []
    playlist_link = input('enter playlist link: ')
    playlist = sp.playlist_tracks(playlist_link)
    l = len(playlist['items'])

    for i in playlist['items']:
        name = i['track']['name']
        artist = i['track']['artists'][0]['name']
        album = i['track']['album']['name']

        test.append(name)
        ur = i['track']['album']['images'][0]['url']
        pdownload(ur, name)

        url = searchYoutube(name+" "+artist + " Audio ")

        Download(url, name.replace(' ', '-'), path)
        audiofile = eyed3.load(path+'/'+name.replace(' ', '-')+'.mp3')
        if (audiofile.tag == None):
            audiofile.initTag()
        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(
            'images/'+name+'.jpg', 'rb').read(), 'image/jpeg')
        audiofile.tag.artist = artist
        audiofile.tag.title = name
        audiofile.tag.album = album
        audiofile.tag.save()
        os.system('clear')
        print(playlist['items'].index(i)+1 * (100/l), '% done')

    print(test)


def single(path):
    song = search.Search(input("Enter Song (with artist name): "))
    name = song.get('name')
    artist = song.get('artist')
    album = song.get('album')
    print("Info Recieved")
    url = searchYoutube(name+" "+artist + " Audio ")
    ur = song.get('image')
    print("getting song from youtube")
    pdownload(ur, name)
    print("Downloaded the image")
    Download(url, name.replace(' ', '-'), path)
    print("Downloaded the song")
    audiofile = eyed3.load(path+'/'+name.replace(' ', '-')+'.mp3')
    if (audiofile.tag == None):
        audiofile.initTag()
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(
        'images/'+name+'.jpg', 'rb').read(), 'image/jpeg')
    audiofile.tag.artist = artist
    audiofile.tag.title = name
    audiofile.tag.album = album
    audiofile.tag.save()
    print("Done")

def Single(name,artist,album,ur, path):
    
    print("Info Recieved")
    url = searchYoutube(name+" "+artist + " Audio ")
    print("getting song from youtube")
    pdownload(ur, name)
    print("Downloaded the image")
    Download(url, name.replace(' ', '-'), path)
    print("Downloaded the song")
    audiofile = eyed3.load(path+'/'+name.replace(' ', '-')+'.mp3')
    if (audiofile.tag == None):
        audiofile.initTag()
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(
        'images/'+name+'.jpg', 'rb').read(), 'image/jpeg')
    audiofile.tag.artist = artist
    audiofile.tag.title = name
    audiofile.tag.album = album
    audiofile.tag.save()
    print("Done")
# if "single" in x:
#     single()
# else:
#     playlist()
# os.system('clear')
# print("Operation Completed thank You For Using The App")
def Playlist(playlist_link, path):
    test = []
    
    playlist = sp.playlist_tracks(playlist_link)
    l = len(playlist['items'])

    for i in playlist['items']:
        name = i['track']['name']
        artist = i['track']['artists'][0]['name']
        album = i['track']['album']['name']

        test.append(name)
        ur = i['track']['album']['images'][0]['url']
        pdownload(ur, name)

        url = searchYoutube(name+" "+artist + " Audio ")

        Download(url, name.replace(' ', '-'), path)
        audiofile = eyed3.load(path+'/'+name.replace(' ', '-')+'.mp3')
        if (audiofile.tag == None):
            audiofile.initTag()
        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(
            'images/'+name+'.jpg', 'rb').read(), 'image/jpeg')
        audiofile.tag.artist = artist
        audiofile.tag.title = name
        audiofile.tag.album = album
        audiofile.tag.save()
        os.system('clear')
        print(playlist['items'].index(i)+1 * (100/l), '% done')
    print(test)

