#!/usr/bin/node
 
const args = process.argv.slice(2)
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/1/', (error, response, body) => {
  if (error) {
    // Handle errors
    console.error('Error:', error);
  } else {
    // Handle the response body
    console.log('Response:', body);
  }
});
