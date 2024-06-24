// Students Controller
import readDatabase from "../utils.js"

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const studentsObject = await readDatabase('database.csv');
      let output = 'This is the list of our students\n';

      output += `Number of students in CS: ${studentsObject.firstNamesCS.length}. List: ${studentsObject.firstNamesCS.join(', ')}\n`;
      output += `Number of students in SWE: ${studentsObject.firstNamesSWE.length}. List: ${studentsObject.firstNamesSWE.join(', ')}`;

      res.status(200).send(output);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { majorto: major } = req.params;

    try {
      const studentsObject = await readDatabase('database.csv');
      let output = '';

      if (major === 'CS') {
        output += `List: ${studentsObject.firstNamesCS.join(', ')}`;
      } else if (major === 'SWE') {
        output += `List: ${studentsObject.firstNamesSWE.join(', ')}`;
      } else {
        return res.status(500).send('Major parameter must be CS or SWE');
      }

      res.status(200).send(output);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
