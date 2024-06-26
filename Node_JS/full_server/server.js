import express from 'express';
import routes from './routes/index.js';

const app = express();
const port = 1245;

routes(app);

app.listen(port);

export default app;
