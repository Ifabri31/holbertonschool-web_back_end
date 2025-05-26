const { readDatabase } = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const db = process.argv[2];
    console.log(`Reading database from: ${db}`);
    readDatabase(db)
      .then((fields) => {
        let response = 'This is the list of our students\n';

        const sortedFields = Object.keys(fields).sort();

        sortedFields.forEach((field) => {
          response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
        });

        res.status(200).send(response);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const db = process.argv[2];
    const { major } = req.params;

    if (!['CS', 'SWE'].includes(major.toUpperCase())) {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    return readDatabase(db)
      .then((fields) => {
        const studentsInMajor = fields[major.toUpperCase()];

        if (!studentsInMajor) {
          return res.status(500).send('Cannot load the database');
        }

        return res.status(200).send(`List: ${studentsInMajor.join(', ')}`);
      })
      .catch(() => res.status(500).send('Cannot load the database'));
  }
}

module.exports = StudentsController;
