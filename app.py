from flask import *
from search import SearchAll
from main import Single, Playlist
import os
import sys
from pathlib import Path
import webbrowser

app = Flask(__name__)

indexFile = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    a{
      text-decoration: none;
      color: white;
    }
    .card{
      background-color: crimson;
      padding-top: 100px;
      padding-bottom: 100px;
      padding-left: 200px;
      padding-right: 200px;
      margin-bottom: 20px;
      width: 50%;
      font-size: 30px;
      text-align: center;
      font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    }
    .container{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
  </style>
</head>
<body>
  <div class = 'container'>
    <a href="/playlist">
      <div class = "card">
        Download A Playlist
      </div>
    </a>
    <a href="/single">
      <div class = "card">
        Download A Song
      </div>
    </a>
  </div>
  
</body>
</html>
"""

playlistFile = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        form{
            position: absolute;
            top:50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding: 20px;
        }
        form input{
            margin: 20px;
        }
        form button{
            margin: 20px;
        }
        form h1{
            margin: 20px;
        }
        form p{
            margin: 20px;
        }
    </style>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
<form class="form-inline my-2 my-lg-0" method = "POST">
    <h1>Link to Public Spotify Playlist</h1>
    <p>Note: Downloading will be finished when the page completely loads</p>
        <input class="form-control mr-sm-2" name = "link"type="search" placeholder="Enter Link..." aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Submit</button>
      </form>
</body>
</html>
"""

selectPathFile = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        form{
            position: absolute;
            top:50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding: 20px;
        }
        form input{
            margin: 20px;
        }
        form button{
            margin: 20px;
        }
        form h1{
            margin: 20px;
        }
    </style>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
<form class="form-inline my-2 my-lg-0" method = "POST">
    <h1>Kindly Provide the path to where you want to save the downloaded files</h1>
        <input class="form-control mr-sm-2" name = "path"type="search" placeholder="Enter Path" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Submit</button>
      </form>
</body>
</html>
"""

singleFile = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
    </style>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body style = "background-color: #212529;">
    {% if success == True %}
    <div class="alert alert-success" role="alert">
        Downloaded successfully
      </div>
    {% endif %}
  <table class="table table-dark" style = "width: 70%;
  margin-left: 15%; border: none;
  ">
  <div class = 'container' >
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
     
        <form  method = "POST" class="form-inline my-2 my-lg-0">
          <input style = "background-color: #212529; color : white;"class="form-control mr-sm-2" name = "search" type="search" placeholder="Search" aria-label="Search">
          <button style = "margin-left: 30px;" class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
    </nav>
    <thead>
      <tr>
        <th scope="col"></th>
        <th scope="col">Title</th>
        <th scope="col">Artist</th>
        <th scope="col">Album</th>
        <th scope="col"></th>
      </tr>
    </thead>
    <tbody>
      <!-- <form class="form-inline my-2 my-lg-0" name = "search" methods = "POST">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form> -->
      <!-- <form method = "post" display = "inline" class = 'form-inline'>
        <div class="mb-3">
          <input type="text" name = "search" class="form-control" id="search" aria-describedby="emailHelp">
        </div>
  
        <button type="submit" class="btn btn-primary">Submit</button>
      </form> -->
      {% for i in data %}
        <tr>
          
          <th><img width = 50 height = 50 src="{{ i['image'] }}" alt=""></th>
            <td><a href=""></a>{{ i['name'] }}</td>
            <td>{{ i['artist'] }}</td>
            <td>{{ i['album'] }}</td>
            <td><a href="/download?title={{i['name'].replace(' ', '-')}}&artist={{i['artist'].replace(' ', '-')}}&album={{i['album'].replace(' ', '-')}}&image={{i['image']}}"><i class="bi bi-download"></i></a></td>
        </tr>
      {% endfor %}
      
    </tbody>
  </table>
  </div>
  

</body>
</html>
"""

if not os.path.exists(str(Path(__file__).parent)+'/templates'):
    os.mkdir(str(Path(__file__).parent)+'/templates')
    with open(str(Path(__file__).parent)+'/templates/index.html', 'w') as file:
        file.write(indexFile)
    with open(str(Path(__file__).parent)+'/templates/playlist.html', 'w') as file:
        file.write(playlistFile)
    with open(str(Path(__file__).parent)+'/templates/selectpath.html', 'w') as file:
        file.write(selectPathFile)
    with open(str(Path(__file__).parent)+'/templates/single.html', 'w') as file:
        file.write(singleFile)

print(Path(__file__))
print(os.listdir(os.path.join(Path(__file__).parent, 'templates')))

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
    if sys.platform == "darwin" or sys.platform == 'Darwin':
        os.system('open {}.mp3'.format(path+"/"+request.args['title']))
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
    webbrowser.open('http://127.0.0.1:5555/')
    app.run(debug=True, port =5555)
    