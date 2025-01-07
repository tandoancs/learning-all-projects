const bcrypt = require('bcryptjs');
const User = require('../models/User');

module.exports = {
    registerView: (req, res) => {
        res.render('register');
    },

    loginView: (req, res) => {
        res.render('login');
    },

    registerUser: async (req, res) => {
        const { name, email, password } = req.body;
        if (!name || !email || !password) {
            return res.render('register', { error: 'Please fill all fields' });
        }

        if (await User.findOne({ where: { email } })) {
            return res.render('register', { error: 'A user account already exists with this email' });
        }

        await User.create({ name, email, password: bcrypt.hashSync(password, 8) });

        res.redirect('login?registrationdone');
    },

    loginUser: (req, res) => {
        // TODO: complete
        res.redirect('login');
    },

    logoutUser: (req, res) => {
        // TODO: complete
        res.redirect('login');
    }
}