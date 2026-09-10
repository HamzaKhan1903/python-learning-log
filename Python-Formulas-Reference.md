# Python Formulas & Syntax Reference — Week 1 Complete (Day 1-6)

*Syntax patterns and formulas only. For the "why" behind each, see Python-Concepts-and-Projects.md*

---

## Checking Type & Identity
```python
type(x)        # returns the type of the object x points to
id(x)          # returns the memory address of the object x points to
x == y         # value equality
x is y         # identity — same object in memory
```

## Type Conversion
```python
int("5")       # str -> int
str(5)         # int -> str
float("3.14")  # str -> float
int(3.9)       # -> 3   (truncates toward zero)
round(3.9)     # -> 4   (rounds to nearest)
```

## Arithmetic / Comparison / Logical Operators
```python
a + b   a - b   a * b   a / b   a // b   a % b   a ** b
a > b   a < b   a >= b   a <= b   a == b   a != b
a and b   a or b   not a
"=" * 40     # string repetition — repeats the string N times
```

---

## Strings
```python
s[0]              # first char (zero-based)
s[-1]             # last char
s[a:b]            # start INCLUDED, end EXCLUDED
s.upper() / .lower() / .strip() / .replace(old,new) / .split()
f"text {variable} {a+b} {amount:.2f}"     # f-strings, code evaluated live, format specs
```

## Conditionals
```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...          # NOT required — chain silently does nothing if no else and nothing matches
bool(x)          # what `if` runs internally — False for 0, 0.0, "", [], {}, set(), None
```

## Loops
```python
for item in my_list:
    ...
for index, item in enumerate(my_list):
    ...
range(5)              # 0,1,2,3,4 — stop excluded
range(2, 10, 2)        # 2,4,6,8 — start, stop, step

total = 0              # accumulator — initialize OUTSIDE the loop
for num in numbers:
    total += num

while condition:
    ...
while True:
    ...
    if exit_condition:
        break          # exits the loop entirely
    if skip_condition:
        continue        # skips rest of THIS pass only, loop continues
```

## Input
```python
x = input("prompt: ")           # ALWAYS returns a string
x = int(input("prompt: "))
x = float(input("prompt: "))
```

---

## Lists
```python
my_list = []
my_list.append(item)
my_list.insert(i, item)
my_list.remove(item)      # first match, ValueError if missing
my_list.pop()              # removes & returns last item
my_list.sort()
my_list.reverse()
```

## Tuples
```python
t = (1, 2, 3)          # immutable
t[0]                    # indexing/slicing works like lists
t[0] = 99               # TypeError — not allowed
```

## Sets
```python
s = {1, 2, 3}          # unordered, no duplicates
s.add(item)
s.remove(item)          # KeyError if missing
s.discard(item)          # safe — no error if missing
a | b     a & b     a - b     # union, intersection, difference
```

## Dictionaries
```python
d = {"key": "value"}
d["key"]                          # KeyError if missing
d.get("key")                       # None if missing
d.get("key", "default")            # custom fallback if missing
d["key"] = new_value               # add OR update — same syntax either way
d["key"] = d["key"] + 1            # read current, add, write back (accumulator pattern)
del d["key"]                        # KeyError if missing, no fallback option
d.pop("key")                        # removes AND returns the value
d.pop("key", "default")             # safe version
"key" in d                          # True/False, no crash
d.keys() / d.values() / d.items()
for k, v in d.items():
    ...
d["a"]["b"]                         # nested dict access, chain brackets
dict(zip(list1, list2))              # build a dict from two parallel lists directly
```

---

## Exception Handling
```python
try:
    risky_code()
except ValueError:
    handle_it()
except KeyError:
    handle_it_differently()
except Exception as e:               # broad catch-all — put LAST, never first
    print("Something went wrong:", e)
```
**Error types and what triggers them:**
| Error | Triggered by |
|---|---|
| `ValueError` | Right type, invalid content — `int("hello")` |
| `TypeError` | Operation invalid for this type — `"a" + 1`, `tuple[0] = x`, list in a set |
| `KeyError` | Dictionary key doesn't exist — `d["missing"]` |
| `ZeroDivisionError` | Dividing by zero — `10 / 0` |
| `NameError` | Using a variable that was never created |
| `IndexError` | List/tuple index out of range |

---

## Comprehensions
```python
squares = [n ** 2 for n in numbers]                       # transform
evens = [n for n in numbers if n % 2 == 0]                  # filter
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]       # transform + filter together

word_lengths = {word: len(word) for word in words}          # dict comprehension
```
Shape: `[expression for item in iterable if condition]` — the `if` is optional.

---

## Menu / Exit Loop Template
```python
while True:
    choice = input("Enter your choice: ")
    if choice == "exit_value":
        break
    elif choice in ("1", "2", "3", "4"):
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount.")
            continue
        if choice == "1":
            ...
        else:
            print("Not implemented yet.")     # defensive inner else
    else:
        print("Invalid choice.")
```

## Collect-Until-Done Loop Template (try/except version)
```python
total = 0
while True:
    entry = input("Enter value or 'done' to finish: ")
    if entry == "done":
        break
    try:
        total += float(entry)
    except ValueError:
        print("Invalid input.")
```