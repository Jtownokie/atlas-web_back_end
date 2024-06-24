// Defined Routes
import app from '../server.js';
import AppController from '../controllers/AppController.js';
import StudentsController from '../controllers/StudentsController.js';

app.get('/', AppController.getHomepage);

app.get('/students', StudentsController.getAllStudents);

app.get('/students/:majorto', StudentsController.getAllStudentsByMajor);
