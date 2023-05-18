from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('reproductor.html')

@app.route('/tracks', methods=['POST'])
def get_tracks():
    client_id = ''
    client_secret = ''
    redirect_uri = 'http://localhost:5000/callback/'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

    artist_name = request.form['artist']
    results = sp.search(q='artist:' + artist_name, type='artist', limit=1)

    if len(results['artists']['items']) > 0:
        artist = results['artists']['items'][0]
        music = sp.artist_top_tracks(artist['uri'])

        tracks = []
        for track in music['tracks'][:10]:
            track_data = {
                'name': track['name'],
                'preview_url': track['preview_url'],
                'cover_art': track['album']['images'][0]['url']
            }
            tracks.append(track_data)

        return {'tracks': tracks}
    else:
        return {'tracks': []}

if __name__ == '__main__':
    app.run(debug=True)
