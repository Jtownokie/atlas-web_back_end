// Task 5 Script
import http from 'http';
import countStudents from './3-read_file_async.js';

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  const { url } = req;

  if (url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (url === '/students') {
    res.write('This is the list of our students\n');

    try {
      const output = await countStudents('database.csv');
      res.write(output);
    } catch (error) {
      res.write(error.message);
    }

    res.end();
  } else {
    res.end();
  }
}).listen(1245);

export default app;
