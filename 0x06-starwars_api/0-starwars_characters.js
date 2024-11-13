#!/usr/bin/node
// Import the required module
const request = require('request');

// Ensure a Movie ID argument is provided
if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Extract the Movie ID from command-line arguments
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch movie details
request(url, async (error, response, body) => {
  if (error) {
    console.error('Error fetching movie:', error);
    return;
  }

  // Parse the response body as JSON
  const data = JSON.parse(body);

  if (!data.characters) {
    console.error('No character data found for this movie.');
    return;
  }

  // Fetch each character's details in order
  for (const characterUrl of data.characters) {
    await new Promise((resolve) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character:', charError);
	  resolve();
	  return;
        }

          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
          resolve();
      });
    });
  }
});
