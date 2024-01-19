#!/usr/bin/node
const args = process.argv.slice(2);
const part = args[0];
const request = require('request-promise-native');

function getData (url) {
  return request(url)
    .then(body => {
      return JSON.parse(body);
    })
}

const url = 'https://swapi-api.alx-tools.com/api/films/' + part + '/';
getData(url)
  .then(data => {
    const charList = data.characters;
    const charPromises = charList.map(charUrl =>
      getData(charUrl)
        .then(charData => {
          return charData.name;
        })
    );
    return Promise.all(charPromises);
  })
  .then(result => {
    for (const name of result) {
      console.log(name);
    }
  })
