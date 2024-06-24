// Task 7 Script

import express from 'express';
import countStudents from './3-read_file_async.js';

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  let output = 'This is the list of our students\n';

  try {
    const studentOutput = await countStudents('database.csv');
    output += studentOutput;
  } catch (error) {
    output += error.message;
  }
  res.send(output);
});

app.listen(port);

export default app;
