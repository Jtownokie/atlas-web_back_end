// Task 3 Script
import { promises as fs } from 'fs';
import { parse } from 'csv-parse';

export default async function countStudents(path) {
  try {
    const fileData = await fs.readFile(path, 'utf8');
    return new Promise((resolve) => {
      parse(fileData, { columns: false, trim: true }, (err, rows) => {
        const numStudents = rows.length - 1;
        let numStudentsInCS = 0;
        let numStudentsInSWE = 0;
        const firstNamesCS = [];
        const firstNamesSWE = [];

        for (const row of rows) {
          if (row[3] === 'CS') {
            numStudentsInCS += 1;
            firstNamesCS.push(row[0]);
          } else if (row[3] === 'SWE') {
            numStudentsInSWE += 1;
            firstNamesSWE.push(row[0]);
          }
        }

        let output = `Number of students: ${numStudents}\n`;
        output += `Number of students in CS: ${numStudentsInCS}. List: ${firstNamesCS.join(', ')}\n`;
        output += `Number of students in SWE: ${numStudentsInSWE}. List: ${firstNamesSWE.join(', ')}`;
        console.log(output);

        resolve(output);
      });
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
