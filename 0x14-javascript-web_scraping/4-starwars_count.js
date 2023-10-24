#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/people/18';

request(
  url,
  function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.films.length);
    }
  }
);
