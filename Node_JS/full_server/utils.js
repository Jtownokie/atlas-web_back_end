// Utility Functions
import { promises as fs } from 'fs';
import { parse } from 'csv-parse';

export default async function readDatabase(path) {
  try {
    const fileData = await fs.readFile(path, 'utf8');
    return new Promise((resolve) => {
      parse(fileData, { columns: false, trim: true }, (err, rows) => {
        const firstNamesCS = [];
        const firstNamesSWE = [];
        const studentsByMajor = {};

        for (const row of rows) {
          if (row[3] === 'CS') {
            firstNamesCS.push(row[0]);
          } else if (row[3] === 'SWE') {
            firstNamesSWE.push(row[0]);
          }
        }

        studentsByMajor.firstNamesCS = firstNamesCS;
        studentsByMajor.firstNamesSWE = firstNamesSWE;

        resolve(studentsByMajor);
      });
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
