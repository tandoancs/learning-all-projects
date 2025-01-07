require('dotenv').config()
console.log(process.env.PORT)

const express = require('express');
const app = express();
const PORT = process.env.PORT || 8080;

app.get('/', (req, res) => res.send('<h1>Hello Express</h1>'));

app.listen(PORT, console.log('Server is running on http://localhost:' + PORT));