#!/usr/bin/node
const request = require('request');

async function getCharacters (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      if (response && response.statusCode === 200) {
        resolve(JSON.parse(body).characters);
      }
    });
  });
}

async function getCharacterName (characterURL) {
  return new Promise((resolve, reject) => {
    request.get(characterURL, (error, response, body) => {
      if (error) reject(error);
      if (response && response.statusCode === 200) {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

(async function main () {
  const argCount = process.argv.length;
  if (argCount !== 3) {
    process.exit(1);
  }
  const movieId = process.argv[2];
  const STAR_WARS_API_URL = 'https://swapi-api.alx-tools.com/api';
  const url = `${STAR_WARS_API_URL}/films/${movieId}`;
  const characterNames = [];
  const movieCharacters = await getCharacters(url);
  for (let i = 0; i < movieCharacters.length; i++) {
    const characterName = await getCharacterName(movieCharacters[i]);
    characterNames.push(characterName);
  }
  console.log(characterNames.join('\n'));
}());
