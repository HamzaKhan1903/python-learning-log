import sqlite3
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

'''cursor.execute("DELETE FROM employees")
cursor.execute("DELETE FROM departments")
connection.commit()

cursor.execute("INSERT INTO employees (name, salary) VALUES ('Priya', 72000)")   # id 1
cursor.execute("INSERT INTO employees (name, salary) VALUES ('Ravi', 65000)")     # id 2
cursor.execute("INSERT INTO employees (name, salary) VALUES ('Sana', 58000)")      # id 3 — no department
connection.commit()

cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (1, 'Engineering')")
cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (2, 'Sales')")
cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (99, 'Marketing')")  # no matching employee
connection.commit()

cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())
cursor.execute("SELECT * FROM departments")
print(cursor.fetchall())

cursor.execute("SELECT employees.name, departments.department_name FROM employees INNER JOIN departments ON employees.id = departments.employee_id;")
print(cursor.fetchall())

cursor.execute("SELECT employees.name, departments.department_name FROM employees LEFT JOIN departments ON employees.id = departments.employee_id;")
print(cursor.fetchall())

cursor.execute("SELECT employees.name, departments.department_name FROM employees RIGHT JOIN departments ON employees.id = departments.employee_id;")
print(cursor.fetchall())

cursor.execute("SELECT employees.name, departments.department_name FROM departments LEFT JOIN employees ON departments.employee_id = employees.id;")
print(cursor.fetchall())'''

cursor.execute("DELETE FROM employees")
cursor.execute("DELETE FROM departments")
connection.commit()

cursor.execute("INSERT INTO employees (name, salary) VALUES ('Priya', 72000)")   # id 1
cursor.execute("INSERT INTO employees (name, salary) VALUES ('Ravi', 65000)")     # id 2
cursor.execute("INSERT INTO employees (name, salary) VALUES ('Sana', 58000)")      # id 3
cursor.execute("INSERT INTO employees (name, salary) VALUES ('John', 80000)")       # id 4
connection.commit()

cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (1, 'Engineering')")
cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (2, 'Engineering')")
cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (3, 'Sales')")
cursor.execute("INSERT INTO departments (employee_id, department_name) VALUES (4, 'Sales')")
connection.commit()

cursor.execute("""
    SELECT departments.department_name, AVG(employees.salary)
    FROM employees
    JOIN departments ON employees.id = departments.employee_id
    GROUP BY departments.department_name
    ORDER BY AVG(employees.salary) DESC;
""")
print(cursor.fetchall())

cursor.execute("""
    SELECT departments.department_name, COUNT(employees.name)
    FROM employees
    JOIN departments ON employees.id = departments.employee_id
    GROUP BY departments.department_name
""")
print(cursor.fetchall())

cursor.execute("""
    SELECT departments.department_name, employees.name, COUNT(employees.name)
    FROM employees
    JOIN departments ON employees.id = departments.employee_id
    GROUP BY departments.department_name
""")
print(cursor.fetchall())

cursor.execute("""
    SELECT departments.department_name, GROUP_CONCAT(employees.name), COUNT(employees.name)
    FROM employees
    JOIN departments ON employees.id = departments.employee_id
    GROUP BY departments.department_name
""")
print(cursor.fetchall())

cursor.execute("SELECT name, salary FROM employees ORDER BY salary DESC;")
print(cursor.fetchall())

cursor.execute("""SELECT departments.department_name, AVG(employees.salary)
FROM employees
JOIN departments ON employees.id = departments.employee_id
GROUP BY departments.department_name
HAVING AVG(employees.salary) > 68600;""")
print(cursor.fetchall())

'''print("--- Testing multiple statements in one execute() ---")
cursor.execute("SELECT * FROM employees; SELECT * FROM departments;")
print(cursor.fetchall())'''
print("--- Using executescript() for multiple statements ---")
cursor.executescript("""
    DELETE FROM employees;
    DELETE FROM departments;
""")
connection.commit()
print("Both tables cleared")