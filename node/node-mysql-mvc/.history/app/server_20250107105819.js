import 'dotenv/config'
import express from 'express';
const app = express();
const PORT = 8080;

app.get('/', (req, res) => res.send('<h1>Hello Express</h1>'));

app.listen(PORT, console.log('Server is running on port: ' + PORT));