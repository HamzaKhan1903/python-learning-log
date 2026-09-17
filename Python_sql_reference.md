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

## JOIN Types — INNER, LEFT, RIGHT

Plain `JOIN` defaults to `INNER JOIN`. Tested directly against a dataset with a deliberate mismatch: Sana (employee, no department) and Marketing (department, no employee).

**INNER JOIN — only rows with a match on BOTH sides:**
```sql
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.id = departments.employee_id;
```
Result: `[('Priya', 'Engineering'), ('Ravi', 'Sales')]` — Sana and Marketing both silently excluded entirely, since neither has a matching row on the other side.

**LEFT JOIN — every row from the LEFT (FROM) table, NULL fills any missing right-side match:**
```sql
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.id = departments.employee_id;
```
Result: `[('Priya', 'Engineering'), ('Ravi', 'Sales'), ('Sana', None)]` — Sana now included, with `None` (SQL's `NULL`) where a department would be.

**RIGHT JOIN — every row from the RIGHT table, NULL fills any missing left-side match:**
```sql
-- SQLite does NOT support RIGHT JOIN natively (OperationalError).
-- Workaround: swap which table is written first, and use LEFT JOIN instead.
SELECT employees.name, departments.department_name
FROM departments
LEFT JOIN employees ON departments.employee_id = employees.id;
```
Result: `[('Priya', 'Engineering'), ('Ravi', 'Sales'), (None, 'Marketing')]` — Marketing now included, `None` where an employee would be. Logically identical to a true `RIGHT JOIN`, just rephrased as a `LEFT JOIN` with the tables swapped.

**When to use which:**
- `INNER JOIN` — only care about complete, matched pairs (e.g. "employees who currently have a department").
- `LEFT JOIN` — the left table is the primary list; want everything in it regardless of a match (e.g. "every employee, with department if they have one" — usually the more complete, honest business question).

**Caution:** defaulting to `INNER JOIN` out of habit is a common real mistake — it silently drops unmatched rows with zero warning, exactly like an `if`/`elif` chain with no `else`. If a report seems to be missing data nobody can explain, an accidental `INNER JOIN` where a `LEFT JOIN` was needed is a frequent real cause.

**Cross-database note:** `RIGHT JOIN`/`FULL OUTER JOIN` support varies by database engine — SQLite lacks both; PostgreSQL/MySQL 8+/SQL Server support `RIGHT JOIN`. Core SQL (`SELECT`, `WHERE`, `INNER JOIN`, `LEFT JOIN`) is portable; some specific features are not.

**Passing multi-line SQL to `cursor.execute()`:** must be one string — either squeezed onto one line inside `"..."`, or spanning multiple lines using triple quotes (`"""..."""`), same as any other Python string. `cursor.execute()` only ever runs ONE statement per call (tested directly — two `SELECT`s in one string raises `ProgrammingError`), partly a deliberate security measure against SQL injection. For multiple statements that don't need results back (e.g. setup/cleanup), use `cursor.executescript("""stmt1; stmt2;""")` instead — for multiple `SELECT`s where you need each result, just call `execute()` + `fetchall()` separately per query.

---

## GROUP BY & Aggregate Functions

**Generic syntax:**
```sql
SELECT column, AGGREGATE_FUNCTION(column)
FROM table
GROUP BY column;
```

**Real example — average salary per department:**
```python
cursor.execute("""
    SELECT departments.department_name, AVG(employees.salary)
    FROM employees
    JOIN departments ON employees.id = departments.employee_id
    GROUP BY departments.department_name
""")
print(cursor.fetchall())
# [('Engineering', 68500.0), ('Sales', 69000.0)]
```
`GROUP BY` collapses multiple rows sharing the same value into ONE summary row per group. Output shape: one row per group, not per original row.

**Common aggregate functions (same pattern, swap the function name):**
```sql
COUNT(column)    -- how many rows in each group
SUM(column)       -- total, not average
AVG(column)        -- average
MAX(column)         -- highest value in the group
MIN(column)          -- lowest value in the group
GROUP_CONCAT(column)  -- SQLite: combines every value in the group into one comma-separated string
                          -- (PostgreSQL equivalent: STRING_AGG — function name varies by database)
```

⚠️ **Real, tested gotcha:** selecting a plain, non-aggregated column alongside `GROUP BY` (e.g. `SELECT department_name, employees.name ... GROUP BY department_name`) does NOT error in SQLite — it silently returns just ONE arbitrary value from the group (whichever row it happened to encounter first), discarding the rest, with zero warning. Only select columns that are either the `GROUP BY` column itself, or wrapped in an aggregate function — anything else gives a misleading, unreliable result.

---

## ORDER BY

**Generic syntax:**
```sql
SELECT columns FROM table ORDER BY column DESC;
```

**Real example:**
```sql
SELECT name, salary FROM employees ORDER BY salary DESC;

SELECT departments.department_name, AVG(employees.salary)
FROM employees
JOIN departments ON employees.id = departments.employee_id
GROUP BY departments.department_name
ORDER BY AVG(employees.salary) DESC;
```
`DESC` = highest to lowest. `ASC` (or omitted — it's the default) = lowest to highest. Can sort directly by an aggregate function's result, not just a plain column.

---

## WHERE vs HAVING

`WHERE` filters individual rows **before** grouping happens — aggregate functions don't exist yet at that stage, so `WHERE AVG(...)` is not valid.
`HAVING` filters **after** grouping/aggregation — this is the correct tool for "only show groups where [aggregate condition]."

```sql
SELECT departments.department_name, AVG(employees.salary)
FROM employees
JOIN departments ON employees.id = departments.employee_id
GROUP BY departments.department_name
HAVING AVG(employees.salary) > 68600;
```

**SQL clause precedence — two separate orders, worth not confusing:**

*Mandatory WRITING order (syntax rule):*
```
SELECT → FROM → JOIN → WHERE → GROUP BY → HAVING → ORDER BY
```

*Actual LOGICAL processing order (what happens first, internally):*
```
1. FROM / JOIN  →  2. WHERE  →  3. GROUP BY  →  4. aggregate functions calculated  →  5. HAVING  →  6. ORDER BY (last)
```
This is exactly why `ORDER BY` can reference an aggregate like `AVG(...)` even though it's "defined" in the `SELECT` line — by the time `ORDER BY` actually runs (last, logically), the aggregate values already exist.

The semicolon `;` just marks the end of one complete SQL statement — not tied to any specific clause.

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