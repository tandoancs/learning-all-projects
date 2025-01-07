// import 'dotenv/config'
var dotenv = require('dotenv');
dotenv.load();
console.log('config')

const express = require('express');
const app = express();
const PORT = process.env.PORT || 8080;

app.get('/', (req, res) => res.send('<h1>Hello Express</h1>'));

app.listen(PORT, console.log('Server is running on port: ' + PORT));