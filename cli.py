import * from main

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
        os.remove('images/'+name+".jpg")
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
    os.remove('images/'+name+".jpg")
    print("Done")