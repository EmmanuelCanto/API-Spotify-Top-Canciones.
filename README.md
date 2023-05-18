# API-Spotify-Top-Canciones.
El proyecto consiste en desarrollar un reproductor de música en línea con integración de la plataforma de streaming de música Spotify. El objetivo es crear una interfaz de usuario funcional que permita a los usuarios reproducir canciones y ver información detallada sobre los artistas y las pistas.

En la parte del backend, utilizaremos Python junto con el framework Flask para crear un servidor web que actúe como intermediario entre el frontend y la API de Spotify. El servidor Flask se encargará de manejar las solicitudes del cliente, interactuar con la API de Spotify y proporcionar los datos necesarios al frontend.

Utilizaremos la biblioteca Spotipy, que es un cliente Python para la API de Spotify, para realizar la autenticación y autorización con Spotify. Esto permitirá acceder a la biblioteca de canciones de un usuario y obtener información detallada sobre las pistas y los artistas.

En el backend, implementaremos rutas en Flask que se encargarán de recibir las solicitudes del frontend, interactuar con la API de Spotify utilizando Spotipy y devolver los datos necesarios en formato JSON. Por ejemplo, tendremos una ruta para obtener la lista de canciones de un artista específico, otra ruta para obtener información detallada sobre una canción en particular, entre otras.

Además, implementaremos la lógica necesaria para manejar las solicitudes de reproducción de canciones. Por ejemplo, cuando el usuario seleccione una canción para reproducir desde el frontend, el servidor Flask se encargará de enviar los comandos adecuados a la API de Spotify para reproducir la canción en el reproductor del usuario.
