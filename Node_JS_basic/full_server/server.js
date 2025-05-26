const express = require('express');
const indexRoutes = require('./routes/index');

const app = express();

app.use(indexRoutes);

const PORT = 1245;

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

module.exports = app;
