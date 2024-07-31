// app.js
 const express = require('express');
 const bodyParser = require('body-parser');
 const mongoose = require('mongoose');
 const taskRoutes = require('./routes/taskRoutes');
 const eventRoutes = require('./routes/eventRoutes');
 const noteRoutes = require('./routes/noteRoutes');
 const authMiddleware = require('./middleware/authMiddleware');

 const app = express();

 // Middleware
 app.use(bodyParser.json());

 // Routes
 app.use('/api/tasks', authMiddleware, taskRoutes);
 app.use('/api/events', authMiddleware, eventRoutes);
 app.use('/api/notes', authMiddleware, noteRoutes);
 module.exports = app;
