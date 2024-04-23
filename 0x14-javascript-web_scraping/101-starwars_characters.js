const request = require('request');

function fetchFilmCharacters (movieId) {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

  request({ url: filmUrl, json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching film:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Failed to fetch film with status code:', response.statusCode);
      return;
    }

    const characters = body.characters;
    characters.forEach(characterUrl => {
      request({ url: characterUrl, json: true }, (error, response, body) => {
        if (error) {
          console.error('Error fetching character:', error);
          return;
        }
        if (response.statusCode !== 200) {
          console.error('Failed to fetch character with status code:', response.statusCode);
          return;
        }
        console.log(body.name);
      });
    });
  });
}

// Process command-line arguments to get the movieId
if (process.argv.length > 2) {
  const movieId = process.argv[2];
  fetchFilmCharacters(movieId);
} else {
  console.log('Usage: node fetchStarWarsCharacters.js <movie_id>');
}
