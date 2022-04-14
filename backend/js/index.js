// creates connection to mysql
const { createPool } = require("mysql");

// creates connection to database
const pool = createPool({
  host: "localhost",
  user: "abdulmalik",
  password: "0213748346Ll!",
  database: "rain_sa_employees",
});

// func to create db
createDB = () => {
  // query is for the sql command you run
  pool.query(
    `CREATE DATABASE IF NOT EXISTS rain_employees`,
    // takes 3 arguments
    (err, result, fields) => {
      if (err) {
        console.log(err);
      }
      return console.log(result);
    }
  );
};
// calls func
// createDB();

// creates a table in the db
employeeTable = () => {
  pool.query(
    `CREATE TABLE IF NOT EXISTS rain_employees(
    employee_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    fullName VARCHAR(150) NOT NULL, 
    cell VARCHAR(10),
    email VARCHAR(200) NOT NULL UNIQUE,
    password VARCHAR(20) NOT NULL
  )`,
    (err, result, fields) => {
      if (err) {
        console.log(err);
      }
      return console.log(result);
    }
  );
};
employeeTable();

addEmployee = () => {
  // id =
  pool.query(
    `INSERT INTO rain_employees (fullName, cell, email, password) VALUES (%s,%s,%s,%s)`,
    // (
    //   id,
    //   fullName,
    //   cell,
    //   email,
    //   password
    // )
    (err, result, fields) => {
      if (err) {
        console.log(err);
      }
      if (result) {
        return console.log(result);
      }
      if (fields) {
        return fields;
      }
    }
  );
};
addEmployee();

// ********************************* //

// check all databases

// pool.query(`SHOW DATABASES`, (err, result, fields) => {
//   if (err) {
//     console.log(err);
//   }
//   return console.log(result);
// });

module.exports = pool;
