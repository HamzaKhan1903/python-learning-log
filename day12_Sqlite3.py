print("--- Setting up a real SQLite database ---")
import sqlite3  #importing sqlite3

connection = sqlite3.connect("company.db") # establishing connection to db while creating it 
cursor = connection.cursor()        #pointing the cursor to that db through connection

#creating table - employees; adding columns id, name, salary with data types and primary key
cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER)")
connection.commit()

#cursor.execute("INSERT INTO employees (name, salary) VALUES ('Ravi', 72000)")
#connection.commit()

cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()
print(results)

cursor.execute("CREATE TABLE IF NOT EXISTS departments (id INTEGER PRIMARY KEY, employee_id INTEGER, department_name TEXT)")
connection.commit()

'''cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (1, 'Engineering')")
cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (2, 'Sales')")
connection.commit()
cursor.execute("SELECT * FROM departments")
results = cursor.fetchall()
print(results)

cursor.execute("""
    SELECT employees.name, employees.salary, departments.department_name
    FROM employees
    JOIN departments ON employees.id = departments.employee_id
""")
joined_results = cursor.fetchall()
print(joined_results)'''
print("--- Cleanup: clearing duplicate department rows ---")
cursor.execute("DELETE FROM departments")
connection.commit()

cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (1, 'Engineering')")
cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (2, 'Sales')")
connection.commit()

cursor.execute("SELECT * FROM departments")
print(cursor.fetchall())

cursor.execute("""
    SELECT employees.name, employees.salary, departments.department_name
    FROM employees
    JOIN departments ON employees.id = departments.employee_id
""")
joined_results = cursor.fetchall()
print(joined_results)