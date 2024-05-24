#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
/**
 * exactOrder: recursive function that prints the name of each character
 * from the array of actors in the order they appear in the array
 * @param {array} actors - an array of character urls
 * @param {number} x - the current index in the array
 */
const exactOrder = (actors, x) => {
  // base case: if we've reached the end of the array, return
  if (x === actors.length) return;

  // make a request to get the character at the current index
  request(actors[x], function (err, res, body) {
    // handle errors
    if (err) throw err;
    
    // print the name of the character
    console.log(JSON.parse(body).name);

    // recursively call the function with the next index
    exactOrder(actors, x + 1);
  });
};
