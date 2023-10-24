#!/usr/bin/node
const request = require('request');

request(
  process.argv[2],
  function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const films = JSON.parse(body).results;
      const filtterdFilms = films.filter(
        function (film) {
          return film.characters.includes(
            'https://swapi-api.alx-tools.com/api/people/18/'
          );
        }
      );

      console.log(filtterdFilms.length);
    }
  }
);
