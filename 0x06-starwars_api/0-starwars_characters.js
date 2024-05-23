#!/usr/bin/node

const request = require('request');

function getCharacterName(url) {
  request(url, function(error, response, body) {
    if (!error && response.statusCode == 200) {
      const json = JSON.parse(body);
      console.log(json.name);
    }
  });
}

function getCharactersInMovie(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, function(error, response, body) {
    if (!error && response.statusCode == 200) {
      const json = JSON.parse(body);
      for (let character of json.characters) {
        getCharacterName(character);
      }
    }
  });
}

const movieId = process.argv[2];
getCharactersInMovie(movieId);
