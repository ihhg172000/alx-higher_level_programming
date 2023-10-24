#!/usr/bin/node
const request = require('request');

request(
  process.argv[2],
  function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const films = JSON.parse(body).results;
      let count = 0;

      films.forEach(film => {
        film.characters.forEach(character => {
          if (character.endsWith('/18/')) {
            count++;
          }
        });
      });

      console.log(count);
    }
  }
);
