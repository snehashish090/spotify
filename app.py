from flask import *
from search import SearchAll
from main import Single, Playlist
import os
import sys
from pathlib import Path

app = Flask(__name__)


print(Path(__file__))
print(os.listdir(os.path.join(Path(__file__).parent, 'templates')))

@app.route('/single', methods = ['GET', 'POST'])
def home():
    with open('config.json', 'r') as file:
        vara = json.load(file)

    if vara == []:
        return redirect('/select')
            
    if request.method == 'POST':
        w = request.form.get('searchbar')
        x = SearchAll(w)
        return render_template('single.html', data = x)

    else:
        return render_template('single.html', data = [])

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == "POST":
        query = request.form.get('searchbar')
        x = SearchAll(query)
        return render_template('single.html', data = x)
    else:
        return 'Hello World'


@app.route('/playlist', methods = ['GET', 'POST'])
def playlist():
    with open('config.json', 'r') as file:
        vara = json.load(file)

    if vara == []:
        return redirect('/select')
    if request.method == 'POST':
        link = request.form.get('link')
        Playlist(link, path = vara[0])
        return 'Completed'
    else:
        return render_template('playlist.html')

@app.route('/play', methods = ['GET', 'POST'])
def play():
    return 'Hello World'


@app.route('/download', methods = ['GET', 'POST'])
def download():
    with open('config.json', 'r') as file:
        path = json.load(file)[0]

    Single(request.args['title'], request.args['artist'], request.args['album'], request.args['image'], path = path)

    filename = '{}.mp3'.format(path+"/"+request.args['title'])
    attachement = send_file(filename, as_attachment=True, download_name=filename)
    os.remove(filename)
    return attachement


@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':

        path = request.form.get('path')
        with open('config.json', 'w') as file:
            json.dump([path], file)

        return redirect('/')
    else:
        return render_template('selectpath.html')
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
