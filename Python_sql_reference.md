# SQL Reference — Categories, Syntax & Python Integration

*Every topic shows the generic syntax template first, then a real working example.*

---

## The Five SQL Command Categories

| Category | Full Name | What it does | Commands |
|---|---|---|---|
| **DDL** | Data Definition Language | Defines/changes database *structure* | `CREATE`, `DROP`, `ALTER`, `TRUNCATE` |
| **DML** | Data Manipulation Language | Changes the actual *data* inside tables | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Data Query Language | *Reads* data without changing anything | `SELECT` (with `WHERE`, `JOIN`, etc. as clauses within it) |
| **DCL** | Data Control Language | Manages *permissions* — who can do what | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | Manages *groups* of changes as one atomic unit | `COMMIT`, `ROLLBACK` |

**Key mental model — SQL is declarative, not procedural:** unlike Python, SQL has no visible `if`/`while` loops. You describe *what result* you want (`WHERE salary > 50000`), and the database figures out *how* to get it internally — conceptually the same job as a Python `for` loop with an `if` check inside it, just hidden from you.

---

## DDL — Data Definition Language

**Generic syntax:**
```sql
CREATE TABLE IF NOT EXISTS table_name (
    column1 TYPE PRIMARY KEY,
    column2 TYPE,
    column3 TYPE
);
```

**Real example:**
```sql
CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER);
```
`IF NOT EXISTS` is a defensive guard — same spirit as `try`/`except FileNotFoundError` in Python — lets you safely re-run the same script without crashing on "table already exists."

**PRIMARY KEY** uniquely identifies each row in its own table (no two rows can share one). If left unspecified in an `INSERT`, SQLite auto-increments it (1, 2, 3...) — conceptually the same idea as a default parameter value in Python.

**Other DDL commands (reference only):**
```sql
DROP TABLE table_name;        -- deletes the entire table AND its data, permanently
ALTER TABLE table_name ADD COLUMN new_column TYPE;   -- adds a column to an existing table
TRUNCATE TABLE table_name;      -- removes all rows, keeps the table structure
```

---

## DML — Data Manipulation Language

**INSERT — generic syntax:**
```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```

**Real example:**
```sql
INSERT INTO employees (name, salary) VALUES ('Priya', 72000);
```
Column names and values must match in order and count — same positional-matching principle as function arguments in Python.

**UPDATE — generic syntax:**
```sql
UPDATE table_name SET column = new_value WHERE condition;
```

**Real example:**
```sql
UPDATE employees SET salary = 60000 WHERE name = 'Ravi';
```
⚠️ **Omitting `WHERE` updates EVERY row in the table** — no error, no warning, just silently applies to everything. Same danger category as an `if`/`elif` chain with no `else`: no crash, just a wrong result nobody's told about.

**DELETE — generic syntax:**
```sql
DELETE FROM table_name WHERE condition;
```

**Real example:**
```sql
DELETE FROM departments WHERE employee_id = 1;
DELETE FROM departments;   -- no WHERE = deletes EVERY row (used deliberately for cleanup/reset)
```

---

## DQL — Data Query Language

**SELECT — generic syntax:**
```sql
SELECT column1, column2 FROM table_name WHERE condition;
SELECT * FROM table_name;    -- * means "every column"
```

**Real examples:**
```sql
SELECT name FROM employees;
SELECT * FROM employees WHERE salary > 50000;
```

**JOIN — generic syntax:**
```sql
SELECT table1.column, table2.column
FROM table1
JOIN table2 ON table1.matching_column = table2.matching_column;
```

**Real example:**
```sql
SELECT employees.name, employees.salary, departments.department_name
FROM employees
JOIN departments ON employees.id = departments.employee_id;
```
A `JOIN` does NOT merge or delete tables — it produces a **combined result set**, pairing rows from two tables wherever the `ON` condition matches. Proven directly: `employees` (id=1, Priya) + `departments` (employee_id=1, Engineering) → combined row `('Priya', 72000, 'Engineering')`.

**FOREIGN KEY** — a column in one table (`departments.employee_id`) that holds the same value as a `PRIMARY KEY` in another table (`employees.id`), creating the actual relationship a `JOIN`'s `ON` clause relies on.

---

## TCL — Transaction Control Language

**Generic syntax:**
```python
connection.commit()     # makes changes permanent
connection.rollback()    # undoes changes if something went wrong
```
Every `INSERT`, `UPDATE`, or `DELETE` needs `.commit()` afterward (via Python's `sqlite3`) to actually persist — without it, changes can be lost. Conceptually the database's own version of "if something goes wrong partway through, undo everything, don't leave things half-done" — same motivation as `try`/`except` in Python, just at the transaction level.

---

## DCL — Data Control Language *(reference only, rarely needed at application level)*

```sql
GRANT SELECT ON employees TO some_user;
REVOKE SELECT ON employees FROM some_user;
```
Managing who can access what — typically a database-admin concern, not something application code usually handles directly.

---

## Python + SQLite Integration

**Generic setup:**
```python
import sqlite3

connection = sqlite3.connect("database_name.db")
cursor = connection.cursor()

cursor.execute("SQL STATEMENT HERE")
connection.commit()          # required after INSERT/UPDATE/DELETE/CREATE

results = cursor.fetchall()    # retrieves query results as a list of tuples
```

**Real example, full working setup:**
```python
import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER)")
connection.commit()

cursor.execute("INSERT INTO employees (name, salary) VALUES ('Priya', 72000)")
connection.commit()

cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()
print(results)     # [(1, 'Priya', 72000)]
```

**Key facts:**
- `sqlite3` is part of Python's standard library — no installation needed, unlike MySQL/PostgreSQL which run as separate server programs. SQLite is a single, self-contained **file** (`company.db`) — same "just a file on disk" idea as `todo.txt` from file handling. The SQL *syntax* itself is nearly identical across SQLite/MySQL/PostgreSQL; what differs is how you connect.
- `connection` and `cursor` are NOT reserved keywords — they're ordinary variable names (could be named anything). What IS fixed is `sqlite3.connect(...)` and `.cursor()` — the actual function/method names the module defines.
- `cursor.execute(...)` runs any SQL statement, passed as a plain string.
- `cursor.fetchall()` returns every row from the last query, as a **list of tuples** — one tuple per row, values in column order. This is why `results[0][1]` would give you the first row's second column, same tuple-indexing rule from Week 1.

---

## Quick Vocabulary Reference

| Term | Definition |
|---|---|
| Table | A structured collection of rows and columns, defined via DDL |
| Row / Record | One entry in a table |
| Column / Field | One piece of data every row has |
| Primary Key | Uniquely identifies each row in its own table |
| Foreign Key | A column referencing another table's primary key — the actual relationship a JOIN uses |
| `WHERE` | Filters rows by a condition — the declarative equivalent of an `if` inside a loop |
| `JOIN` | Combines rows from two tables based on a matching column, for one query — does not merge or delete anything |
| Transaction | A group of changes treated as one atomic unit — `.commit()` to save, `.rollback()` to undo |