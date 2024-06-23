// Task 2 Script
import fs from 'fs';
import { parse } from 'csv-parse';

export default function countStudents(path) {
  try {
    fs.readFile(path, (err, fileData) => {
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

        console.log(`Number of students: ${numStudents}`);
        console.log(`Number of students in CS: ${numStudentsInCS}. List: ${firstNamesCS}`);
        console.log(`Number of students in SWE: ${numStudentsInSWE}. List: ${firstNamesSWE}`);
      });
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
