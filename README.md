# Spotify Downloader


## Step 1: 
Install latest version of python from https://python.org 
## Step 2:
Make sure you have pip installed on your computer

## Step 3:
```
$ git clone https://github.com/snehashish090/spotify
 ```
 ```
 $ cd spotify
 ```
 ```
 $ pip install -r requirements.txt
 ```

## Step 4:

Go to https://developer.spotify.com and create a project. Paste your client id and client secret into the creds.json file. It should look something like
```json
{
    "clientId":"YOUR_CLIENT_ID",
    "clientSecret":"YOUR CLIENT SECRET"
}
```

## Step 5:
Open config.json and configure the path to where you want to store your mp3 files. It should looke somthing like :
```json
[
    '~/Users/username/music/'
]
```

## Final Step
At last run the web application by running. Make sure to run it from the spotify directory. 

```bash
$ python app.py
```
