CREATE TABLE rainDB.rain_employees(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    fullname VARCHAR(100) NOT NULL,
    cell INTEGER NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    password VARCHAR(13) NOT NULL
)

INSERT INTO rain_employees (id, fullname, cell, email, password)
VALUES (
    id:int,
    'fullname:varchar',
    cell:int,
    'email:varchar',
    'password:varchar'
  );

  CREATE TABLE testdb.testtable (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,firstname VARCHAR(100) NOT NULL,lastname VARCHAR(100) NOT NULL,email VARCHAR(200))

INSERT INTO testdb.testtable3 (firstname, lastname, email)
VALUES ( 
    'abdul',
    'mohamed',
    'am@gmail.com'
  );