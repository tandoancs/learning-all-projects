require('dotenv').config()
console.log(process.env.PORT)

const express = require('express');
const authRoutes = require('./routes/auth');
const dashboardRoutes = require('./routes/dashboard');
const db = require('./db.js');


const app = express();
const PORT = process.env.PORT || 8080;

app.use(express.urlencoded({extended: false}));
app.set('view engine', 'pug');
app.use('/', authRoutes);
app.use('/', dashboardRoutes);

// app.get('/', (req, res) => res.render('dashboard'));
// app.get('/login', (req, res) => res.render('login'));
// app.get('/register', (req, res) => res.render('register'));

app.listen(PORT, console.log('Server is running on http://localhost:' + PORT));