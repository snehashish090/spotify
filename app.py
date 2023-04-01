from flask import *
from search import SearchAll
from main import Single, Playlist
import os

app = Flask(__name__)


@app.route('/single', methods = ['GET', 'POST'])
def home():
    with open('config.json', 'r') as file:
        vara = json.load(file)

    if vara == []:
        return redirect('/select')
            
    if request.method == 'POST':
        w = request.form.get('search')
        x = SearchAll(w)
        return render_template('single.html', data = x)

    else:
        return render_template('single.html', data = [])

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')


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

    return redirect('/single')

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
    app.run(debug=True, port =5555)