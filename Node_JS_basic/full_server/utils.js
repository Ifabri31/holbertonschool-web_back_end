const fs = require('fs');


function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8')
      .then(data => {
        try {
          const lines = data.split('\n').filter(line => line.trim() !== '');
          
          const dataLines = lines.slice(1);
          
          const studentsByField = {};
          
          dataLines.forEach(line => {
            const columns = line.split(',');
            
            if (columns.length >= 4) {
              const firstname = columns[0].trim();
              const field = columns[3].trim();
              
              if (!studentsByField[field]) {
                studentsByField[field] = [];
              }
              
              studentsByField[field].push(firstname);
            }
          });
          
          resolve(studentsByField);
        } catch (parseError) {
          reject(new Error(`Error parsing file: ${parseError.message}`));
        }
      })
      .catch(error => {
        reject(error);
      });
  });
}

module.exports = readDatabase;
