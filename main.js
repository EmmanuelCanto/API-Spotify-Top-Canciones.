document.addEventListener("DOMContentLoaded", function() {
    // Obtén una referencia a los elementos de la canción en el reproductor
    var songTitleElement = document.querySelector(".song-title");
    var songArtistElement = document.querySelector(".song-artist");
  
    // Define la función para actualizar la información de la canción
    function actualizarInformacionCancion(cancion) {
      songTitleElement.textContent = cancion.titulo;
      songArtistElement.textContent = cancion.artista;
    }
  
    // Obtén la lista de canciones desde el código Python
    var canciones = [
      {
        titulo: "Canción 1",
        artista: "Artista 1"
      },
      {
        titulo: "Canción 2",
        artista: "Artista 2"
      },
      // ...agrega más canciones según lo que te devuelva el código Python
    ];
  
    // Actualiza la información de la primera canción en el reproductor
    if (canciones.length > 0) {
      actualizarInformacionCancion(canciones[0]);
    } else {
      // Si no hay canciones, muestra un mensaje
      songTitleElement.textContent = "No se encontraron canciones.";
      songArtistElement.textContent = "";
    }
  });
  