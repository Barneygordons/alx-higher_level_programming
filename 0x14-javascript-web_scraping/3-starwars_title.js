#!/usr/bin/node
// status of a request
const myRequest = require('request');
const myUrl = 'https://swapi-api.alx-tools.com/api/films/:id' + process.argv[2];
myRequest(myUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonBody = JSON.parse(body);
    console.log(jsonBody.title);
  }
});
