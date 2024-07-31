const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const config = require('./config/config');

const PORT = process.env.PORT || 5000;

	// Create Express app
	const app = express();

	// Middleware
	app.use(bodyParser.json());

	// Connect to MongoDB
	mongoose.connect(config.dbUrl, { useNewUrlParser: true, useUnifiedTopology: true })
		.then(() => console.log('MongoDB connected'))
		.catch(err => console.error('Error connecting to MongoDB:', err));

	// Mock database to store user data (replace with actual database)
	const users = [];
	// Endpoint to handle user sign-up
	app.post('/api/signup', (req, res) => {
	const { username, email, password } = req.body;

	// Check if user already exists
	if (users.some(user => user.email === email)) {
		return res.status(400).json({ error: 'User already exists' });
	}

	// Create new user object
	const newUser = { username, email, password };

	// Add user to the database (or any other appropriate action)
	users.push(newUser);

	// Return success message
	res.status(201).json({ message: 'User created successfully', user: newUser });
	});

	// Start server
	app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

