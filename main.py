import spotipy
from spotipy.oauth2 import SpotifyOAuth

try:

    client_id = 'd866e141f974454da5ebe4a1a7ce0180'
    client_secret = '41047a7593154c45905b12cd5520e731'
    redirect_uri = 'http://localhost:8888/callback/'  # Debes agregar esta URL en la configuración de tu aplicación en Spotify

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

    artist_name = input('Nombre del artista: ')
    results = sp.search(q='artist:' + artist_name, type='artist', limit=1)
    if len(results['artists']['items']) > 0:
        artist = results['artists']['items'][0]
        music = sp.artist_top_tracks(artist['uri'])

    
        for track in music['tracks'][:10]:
            print('track    : ' + track['name'])
            print('audio    : ' + track['preview_url'])
            print('cover art: ' + track['album']['images'][0]['url'])
            print('Géneros:', artist['genres'])
            print('Audio:     : ' + track['preview_url'])
            print()
            print()

    
    
    else:
        print('No se encontro ningun resultado para el artista especificado.')
    
except spotipy.SpotifyException as e:
    print('Ocurrio un error en la conexion con spotify')
