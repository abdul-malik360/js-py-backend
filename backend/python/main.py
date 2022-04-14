import mysql.connector

rainDB = mysql.connector.connect(
    host = 'localhost',
    user = 'abdulmalik',
    password = '0213748346Ll!',
    database = 'rain_employees'
)
# print(rainDB)

rainDB_cursor = rainDB.cursor()

rainDB_cursor.execute("CREATE DATABASE IF NOT EXISTS rain_employees") # DATABASE already created
# rainDB_cursor.execute("SHOW DATABASES")

# table created
# rainDB_cursor.execute("CREATE TABLE employees (employee_id INTEGER AUTO_INCREMENT PRIMARY KEY, fullname VARCHAR(150) NOT NULL, cell INTEGER(13), email VARCHAR(200) NOT NULL UNIQUE, password VARCHAR(20) NOT NULL)")
# rainDB_cursor.execute("SHOW TABLES")
# rainDB_cursor.execute("SELECT * FROM employees")
# for table in rainDB_cursor:
    # print(table[0])
    # print(table)

# add_employee = "INSERT INTO employees (fullname, cell, email, password) VALUES (%s,%s,%s,%s)"
# employee1 = ('Abdul-Malik Mohamed', 764971338, '62545a@gmail.com', 'password')

# rainDB_cursor.execute(add_employee, employee1)
# rainDB.commit()

# add_employees = "INSERT INTO employees (fullname, cell, email, password) VALUES (%s,%s,%s,%s)"
# employees = [
#     ('John Doe', 213474585 , 'john1@gmail.com', '123456'),
#     ('Jane Doe', 824631126, 'jane1@gmail.com', '654321'),
#     ('Achmat Breda', 725698530, 'achmat1@gmail.com', '456789')
# ]

# rainDB_cursor.executemany(add_employees, employees)
# rainDB.commit()


# rainDB_cursor.execute("SELECT * FROM employees")
# employees_list = rainDB_cursor.fetchall()
# for employees in employees_list:
#     # print(employees)
#     break

# rainDB_cursor.execute("SELECT fullname FROM employees")
# employees_list = rainDB_cursor.fetchall()
# for employees in employees_list:
#     # print(employees[0])
#     break

# rainDB_cursor.execute("SELECT * FROM employees")
# employees_list = rainDB_cursor.fetchall()
# print("Id\tFullname\tCell\t\tEmail")
# for employees in employees_list:
#     # print( " %s" %employees[1] + " %s" %employees[2] + " %s" %employees[3] )
#     print("%s"%employees[0] + "\t%s" %employees[1] + "\t%s" %employees[2] + "\t%s" %employees[3] )

# rainDB_cursor.execute("SELECT * FROM employees WHERE employee_id > 5")
# result = rainDB_cursor.fetchall()
# for row in result:
#     print(row)

# rainDB_cursor.execute("SELECT * FROM employees WHERE fullname = 'Abdul-Malik Mohamed'")
# result = rainDB_cursor.fetchall()
# for row in result:
#     print(row)

# rainDB_cursor.execute("SELECT * FROM employees WHERE fullname LIKE '%a'")
# result = rainDB_cursor.fetchall()
# for row in result:
#     print(row)

# rainDB_cursor.execute("SELECT * FROM employees WHERE fullname LIKE '%a' AND employee_id = 11")
# result = rainDB_cursor.fetchall()
# for row in result:
#     print(row)

# rainDB_cursor.execute("SELECT * FROM employees WHERE fullname LIKE '%a' OR employee_id = 11")
# result = rainDB_cursor.fetchall()
# for row in result:
#     print(row)

# rainDB_update = "UPDATE employees SET fullname = 'Abdul' WHERE email =  '62545a@gmail.com'"
# rainDB_cursor.execute(rainDB_update)
# rainDB.commit()

# rainDB_cursor.execute("SELECT * FROM employees LIMIT 4")
# result = rainDB_cursor.fetchall()
# for row in result:
#     print(row)

# rainDB_cursor.execute("SELECT * FROM employees LIMIT 4 OFFSET 2")
# result = rainDB_cursor.fetchall()
# for row in result:
#     print(row)

# rainDB_cursor.execute("SELECT * FROM employees ORDER BY fullname ASC")
# result = rainDB_cursor.fetchall()
# for row in result:
#     print(row)

# rainDB_cursor.execute("SELECT * FROM employees ORDER BY fullname DESC")
# result = rainDB_cursor.fetchall()
# for row in result:
#     print(row)

# rainDB_delete = rainDB_cursor.execute("DELETE FROM employees WHERE employee_id = 9")
# rainDB_cursor.execute(rainDB_delete)
# rainDB.commit() 

# rainDB_drop = "DROP TABLE employees" 
# rainDB_cursor.execute(rainDB_drop)

# rainDB_drop = "DROP TABLE IF EXISTS employees" 
# rainDB_cursor.execute(rainDB_drop)

# add func

# import mysql.connector  

# def addEmployee():
#     rainDB =  mysql.connector.connect(user="abdulmalik", password="0213748346Ll!", host="127.0.0.1", database="rainDB", auth_plugin="mysql_native_password", buffered=True)
#     rainDB_Cursor = rainDB.cursor()
#     # rainDB_Execute = rainDB_Cursor.execute("select * from rain_employees")
#     # print(rainDB_Execute, "consoled!")
#     insert_employee = "INSERT INTO rain_employees (id, fullname, cell, email, password) VALUES (%s,%s,%s,%s,%s)"
#     employee_entry = ('%s,%s,%s,%s,%s')
#     rainDB_Cursor.execute(insert_employee, employee_entry)
#     rainDB.commit()

# # console(rainDB)

# addEmployee()
# # print(addEmployee())