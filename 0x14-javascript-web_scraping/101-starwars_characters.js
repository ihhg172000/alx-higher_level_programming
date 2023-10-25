#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function printCharacters (charactersUrls) {
  let idx = 0;

  function printCharacter (charactersUrl) {
    request(charactersUrl, (error, response, body) => {
      if (!error) {
        const character = JSON.parse(body);

        console.log(character.name);

        try {
          printCharacter(charactersUrls[++idx]);
        } catch {
          // just done
        }
      }
    });
  }

  printCharacter(charactersUrls[idx]);
}

request(url, (error, response, body) => {
  if (!error) {
    const film = JSON.parse(body);
    const charactersUrls = film.characters;

    printCharacters(charactersUrls);
  }
});
